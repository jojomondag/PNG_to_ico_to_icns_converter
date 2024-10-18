#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import sys
import struct

def convert_image(image_path, output_format):
    icon_original_name = "icon"
    icon_extension = output_format.lower()
    output_dir = os.path.dirname(image_path)  # Get the directory of the source image
    icon_name = icon_original_name
    icon_index = 2

    # Construct the initial output path
    output_path = os.path.join(output_dir, f"{icon_name}.{icon_extension}")

    # Avoid overwriting existing files by incrementing the filename
    while os.path.isfile(output_path):
        icon_name = f"{icon_original_name}_{icon_index}"
        output_path = os.path.join(output_dir, f"{icon_name}.{icon_extension}")
        icon_index += 1

    try:
        with Image.open(image_path) as img:
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            if icon_extension == 'ico':
                sizes = [16, 24, 32, 48, 64, 128, 256]
                img.save(output_path, format='ICO', sizes=[(size, size) for size in sizes])
            elif icon_extension == 'icns':
                create_icns(img, output_path)
            else:
                raise ValueError("Unsupported output format.")

        return f"The {icon_extension.upper()} file has been successfully created:\n{output_path}"
    except Exception as e:
        return f"An error occurred while creating the {icon_extension.upper()} file: {str(e)}"

def create_icns(img, output_path):
    # Define the icon types and sizes
    icon_sizes = {
        'icp4': (16, 16),       # 16x16
        'icp5': (32, 32),       # 32x32
        'icp6': (64, 64),       # 64x64
        'ic07': (128, 128),     # 128x128
        'ic08': (256, 256),     # 256x256
        'ic09': (512, 512),     # 512x512
        'ic10': (1024, 1024),   # 1024x1024
    }

    icns_data = b''
    for icon_type, size in icon_sizes.items():
        resized_img = img.resize(size, Image.LANCZOS)
        # Save the image to PNG format in memory
        from io import BytesIO
        png_data_io = BytesIO()
        resized_img.save(png_data_io, format='PNG')
        png_data = png_data_io.getvalue()

        # Build the icon block
        icon_block = icon_type.encode('utf-8') + struct.pack('>I', len(png_data) + 8) + png_data
        icns_data += icon_block

    # ICNS header
    icns_header = b'icns' + struct.pack('>I', len(icns_data) + 8)
    with open(output_path, 'wb') as f:
        f.write(icns_header)
        f.write(icns_data)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        if not file_path.lower().endswith('.png'):
            messagebox.showerror("Error", "Please select a PNG file.")
            return

        ico_result = convert_image(file_path, 'ico')
        icns_result = convert_image(file_path, 'icns')
        messagebox.showinfo("Conversion Result", f"{ico_result}\n\n{icns_result}")

def main():
    root = tk.Tk()
    root.title("PNG to ICO/ICNS Converter")
    root.geometry("400x150")

    label = tk.Label(root, text="Select a PNG file to convert to ICO and ICNS:")
    label.pack(pady=10)

    select_button = tk.Button(root, text="Select PNG", command=select_file)
    select_button.pack()

    info_label = tk.Label(root, text="This will create both ICO and ICNS files in the same directory as the selected PNG.")
    info_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
