#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def convert_image(image_path, output_format):
    icon_original_name = "icon"
    icon_name = icon_original_name
    icon_extension = output_format.lower()

    icon_index = 2
    while os.path.isfile(f"{icon_name}.{icon_extension}"):
        icon_name = f"{icon_original_name}_{icon_index}"
        icon_index += 1

    output_path = f"{icon_name}.{icon_extension}"

    sizes = [16, 32, 48, 64, 128, 256, 512]  # Added 512 to the list of sizes
    images = []

    try:
        with Image.open(image_path) as img:
            for size in sizes:
                resized_img = img.resize((size, size), Image.LANCZOS)
                images.append(resized_img)

        if icon_extension == 'ico':
            images[0].save(output_path, format='ICO', sizes=[(size, size) for size in sizes])
        elif icon_extension == 'icns':
            images[0].save(output_path, format='ICNS', sizes=[(size, size) for size in sizes])
        
        return f"The {icon_extension.upper()} file has been successfully created: ./{output_path}"
    except Exception as e:
        return f"An error occurred while creating the {icon_extension.upper()} file: {str(e)}"

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

    info_label = tk.Label(root, text="This will create both ICO and ICNS files.")
    info_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
