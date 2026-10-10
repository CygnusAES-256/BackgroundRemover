BackgroundRemover

A simple Python application that removes the background from images using rembg.

Select an image through a graphical file dialog, process it automatically, and save the result as a transparent PNG image.

Features
Graphical image selection using Tkinter.
Supports PNG, JPG, JPEG, WEBP, and BMP images.
Automatic background removal with rembg.
Saves the processed image as a PNG with a transparent background.
Keeps the original image unchanged.
Requirements
Python libraries that are not included in the standard library.
A compatible runtime environment for CPU or optional GPU acceleration.
Python libraries

The application uses the following libraries:

Pillow — image loading and saving.
rembg — background removal.
Tkinter — graphical file selection, usually included with Python. Some Linux distributions require a separate system package.

The os module is part of Python's standard library and does not need to be installed separately.

Installation
Clone this repository:
   git clone https://github.com/USERNAME/BackgroundRemover.git
   cd BackgroundRemover

Install the dependencies.

For CPU execution:

   python -m pip install "rembg[cpu]"
   python -m pip install Pillow


For NVIDIA GPU acceleration:

   python -m pip install "rembg[gpu]"
   python -m pip install Pillow


Important: CPU and GPU installations use different ONNX Runtime backends.
