import struct
import sys
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageFile
import io

# Allow loading of truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Mapping of ICO image sizes to ICNS icon types
ICNS_ICON_TYPES = {
    (16, 16): ['is32', 's8mk'],
    (32, 32): ['il32', 'l8mk'],
    (64, 64): ['icp4'],
    (128, 128): ['icp5'],
    (256, 256): ['icp6'],
    (512, 512): ['ic07'],
    (1024, 1024): ['ic08'],
}

def read_ico(file_path):
    with open(file_path, 'rb') as f:
        # Read ICO header
        reserved, ico_type, count = struct.unpack('<HHH', f.read(6))

        if reserved != 0 or ico_type != 1:
            print("Not a valid ICO file.")
            sys.exit(1)

        print(f"Number of images in the ICO file: {count}\n")

        entries = []

        # Read each Icon Directory Entry
        for i in range(count):
            entry = f.read(16)
            width, height, color_count, reserved = struct.unpack('<BBBB', entry[:4])
            planes, bit_count = struct.unpack('<HH', entry[4:8])
            bytes_in_res, image_offset = struct.unpack('<II', entry[8:16])

            # Adjust for 0 width or height (256)
            width = 256 if width == 0 else width
            height = 256 if height == 0 else height

            print(f"Image {i + 1}:")
            print(f"  Width: {width}px")
            print(f"  Height: {height}px")
            print(f"  Color Count: {color_count}")
            print(f"  Color Planes: {planes}")
            print(f"  Bits per Pixel: {bit_count}")
            print(f"  Image Size: {bytes_in_res} bytes")
            print(f"  Image Offset: {image_offset} bytes\n")

            # Save current file position
            current_pos = f.tell()

            # Read image data
            f.seek(image_offset)
            image_data = f.read(bytes_in_res)

            # Determine if image data is PNG or BMP
            if image_data[:8] == b'\x89PNG\r\n\x1a\n':
                img_format = 'PNG'
            else:
                img_format = 'BMP'

            try:
                # Load image using Pillow
                image = Image.open(io.BytesIO(image_data))
                image.load()  # Ensure the image is fully loaded
            except Exception as e:
                print(f"Error loading image {i + 1}: {e}")
                f.seek(current_pos)
                continue

            entries.append({
                'width': width,
                'height': height,
                'color_count': color_count,
                'planes': planes,
                'bit_count': bit_count,
                'bytes_in_res': bytes_in_res,
                'image_offset': image_offset,
                'format': img_format,
                'image_data': image_data,
                'image': image
            })

            # Restore file position
            f.seek(current_pos)

        return entries

def write_icns(entries, output_path):
    icns_header = b'icns'

    # Buffer to hold all icon data entries
    icns_data = bytearray()

    for entry in entries:
        width = entry['width']
        height = entry['height']
        image = entry['image']

        # Find appropriate ICNS icon type
        icon_types = ICNS_ICON_TYPES.get((width, height))

        if not icon_types:
            print(f"Skipping unsupported icon size: {width}x{height}")
            continue

        for icon_type in icon_types:
            try:
                # Prepare image data
                with io.BytesIO() as output:
                    if icon_type in ['icp4', 'icp5', 'icp6', 'ic07', 'ic08']:
                        # Use PNG format for these icon types
                        image.save(output, format='PNG')
                    elif icon_type in ['is32', 'il32']:
                        # 32-bit RGBA data
                        rgba_image = image.convert('RGBA')
                        # ICNS stores image data in big-endian ARGB format
                        data = bytearray()
                        pixels = rgba_image.load()
                        for y in range(rgba_image.height):
                            for x in range(rgba_image.width):
                                r, g, b, a = pixels[x, y]
                                data.extend(struct.pack('>BBBB', a, r, g, b))
                        output.write(data)
                    elif icon_type in ['s8mk', 'l8mk']:
                        # 8-bit alpha mask
                        alpha_image = image.convert('L')
                        output.write(alpha_image.tobytes())
                    else:
                        print(f"Unsupported icon type: {icon_type}")
                        continue

                    icon_data = output.getvalue()

                # Build icon data entry
                entry_size = 8 + len(icon_data)
                icns_data.extend(icon_type.encode('ascii'))
                icns_data.extend(struct.pack('>I', entry_size))
                icns_data.extend(icon_data)
            except Exception as e:
                print(f"Error processing icon type {icon_type} for size {width}x{height}: {e}")
                continue

    if not icns_data:
        print("No valid icon data was generated. ICNS file will not be created.")
        sys.exit(1)

    # Build ICNS file
    total_size = 8 + len(icns_data)

    with open(output_path, 'wb') as f:
        f.write(icns_header)
        f.write(struct.pack('>I', total_size))
        f.write(icns_data)

    print(f"\nICNS file saved to {output_path}")

def main():
    # Hide Tkinter root window
    Tk().withdraw()

    # Ask user to select ICO file
    ico_path = askopenfilename(title="Select ICO File", filetypes=[("ICO files", "*.ico")])

    if not ico_path:
        print("No file selected.")
        sys.exit(1)

    entries = read_ico(ico_path)

    if not entries:
        print("No valid images were extracted from the ICO file.")
        sys.exit(1)

    # Ask user where to save ICNS file
    icns_path = asksaveasfilename(title="Save ICNS File As", defaultextension=".icns", filetypes=[("ICNS files", "*.icns")])

    if not icns_path:
        print("No save location selected.")
        sys.exit(1)

    write_icns(entries, icns_path)

if __name__ == "__main__":
    main()