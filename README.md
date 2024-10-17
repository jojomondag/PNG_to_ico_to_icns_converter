# PNG to ICO and ICNS Converter

This Python script converts PNG files to both Windows ICO and macOS ICNS formats. It provides a graphical user interface for selecting input files, making it easy to use for those who prefer not to use command-line tools.

## Features

- Converts PNG files to both ICO and ICNS formats simultaneously
- Supports multiple image sizes within a single ICO/ICNS file
- Simple graphical user interface for file selection
- Automatically generates output files in the same directory as the script

## Requirements

- Python 3.6+
- Pillow (PIL Fork)
- tkinter (usually comes pre-installed with Python)

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Install the required Pillow library:

```
pip install Pillow
```

3. Download the `png_to_ico_icns_converter.py` script from this repository.

## Usage

1. Run the script:

```
python png_to_ico_icns_converter.py
```

2. A file dialog will open. Select the PNG file you want to convert.
3. The script will process the PNG file and create both ICO and ICNS files in the same directory as the script.

## How It Works

1. The script reads the PNG file and extracts information about each image it contains.
2. It then processes each image and converts it to the appropriate format for ICO and ICNS.
3. The script creates both ICO and ICNS files with the converted images, mapping each image to its corresponding icon type based on size.

## Supported ICNS Icon Types

The script supports the following ICNS icon types:

- 16x16: 'is32' (32-bit RGB image) and 's8mk' (8-bit alpha mask)
- 32x32: 'il32' (32-bit RGB image) and 'l8mk' (8-bit alpha mask)
- 64x64: 'icp4' (PNG format)
- 128x128: 'icp5' (PNG format)
- 256x256: 'icp6' (PNG format)
- 512x512: 'ic07' (PNG format)
- 1024x1024: 'ic08' (PNG format)

## Notes

- The script allows loading of truncated images, which can be helpful for some improperly formatted PNG files.
- If a PNG file contains image sizes that don't match the supported ICNS types, those images will be skipped.
- The script provides detailed output about each image in the PNG file, including dimensions, color depth, and file format.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Author

[Josef Nobach aka jojomondag]
