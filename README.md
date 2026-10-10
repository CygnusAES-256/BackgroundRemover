# BackgroundRemover

A simple Python application that removes image backgrounds using rembg.

Select an image through a graphical file dialog, remove its background, and save the result as a transparent PNG.

## Features

* Select images through a graphical file dialog.
* Supports PNG, JPG, JPEG, WEBP, and BMP.
* Automatically removes backgrounds using rembg.
* Saves the result as a transparent PNG.
* Preserves the original image.

## Requirements

* Python installed on your system.
* Pillow for image processing.
* rembg for background removal.
* Tkinter for the graphical interface. Usually included with Python, but may require separate installation on Linux.
* The os module is part of Python's standard library and does not require separate installation.

## Installation

### 1. Download the code

Choose whichever method you prefer:

* **Clone the repository:**
  git clone https://github.com/USERNAME/BackgroundRemover.git
  cd BackgroundRemover

* **Download the source code only:** Click Code → Download ZIP on the GitHub repository page and extract the downloaded archive. You do not need Git installed for this method.

### 2. Install the dependencies

Choose one of the following configurations.

* **CPU execution**
  python -m pip install "rembg[cpu]" Pillow

* **NVIDIA GPU acceleration**
  python -m pip install "rembg[gpu]" Pillow

GPU acceleration requires compatible hardware, drivers, and runtime components.
