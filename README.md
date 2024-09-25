# ICO to ICNS Converter

This Python script converts Windows ICO files to macOS ICNS files. It provides a graphical user interface for selecting input and output files, making it easy to use for those who prefer not to use command-line tools.

## Features

- Converts ICO files to ICNS format
- Supports multiple image sizes within a single ICO file
- Handles both PNG and BMP formatted images within ICO files
- Provides a user-friendly GUI for file selection
- Displays detailed information about each image in the ICO file

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

3. Download the `ico_to_icns_converter.py` script from this repository.

## Usage

1. Run the script:

```
python ico_to_icns_converter.py
```

2. A file dialog will open. Select the ICO file you want to convert.
3. Another file dialog will open. Choose the location and name for the output ICNS file.
4. The script will process the ICO file and create the ICNS file at the specified location.

## How It Works

1. The script reads the ICO file and extracts information about each image it contains.
2. It then processes each image and converts it to the appropriate format for ICNS.
3. The script creates an ICNS file with the converted images, mapping each image to its corresponding ICNS icon type based on size.

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

- The script allows loading of truncated images, which can be helpful for some improperly formatted ICO files.
- If an ICO file contains image sizes that don't match the supported ICNS types, those images will be skipped.
- The script provides detailed output about each image in the ICO file, including dimensions, color depth, and file format.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Author

[Josef Nobach aka jojomondag]