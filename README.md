<div align="center">
<pre>
██╗███╗   ███╗ ██████╗ ███████╗ ██████╗ ██████╗ ████████╗
██║████╗ ████║██╔════╝ ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
██║██╔████╔██║██║  ███╗███████╗██║   ██║██████╔╝   ██║   
██║██║╚██╔╝██║██║   ██║╚════██║██║   ██║██╔══██╗   ██║   
██║██║ ╚═╝ ██║╚██████╔╝███████║╚██████╔╝██║  ██║   ██║   
╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
-------------------------------------------------
Automated Image Classifier: Sorts grayscale and colored images
</pre>


[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

## Overview
`image-color-classifier` is a simple Python script that automatically classifies images into **colored** and **grayscale**, moving them into separate folders. Ideal for batch processing datasets.

## Installation

Ensure you have Python installed, then install the required dependencies:

```sh
pip install opencv-python
```

## Usage

Place images inside the `data/` folder before running the script.

### Running the script
```sh
python main.py
```


The script processes all images in the `data/` folder and moves them into:
- `colored/` → for colored images 
- `grayed/` → for grayscale images 

### Folder Structure
```sh
📂 Project
 ├── 📂 data       # Input images folder
 ├── 📂 colored    # Classified colored images
 ├── 📂 grayed     # Classified grayscale images
 ├── main.py       # The script
```


##  Features
 - Automatically detects and sorts images
 - Uses OpenCV for fast processing 
 - Works on **Windows, macOS, and Linux** 
 - Lightweight and easy to use 

## License
This project is licensed under the MIT License

## Contributing
Feel free to open issues and submit pull requests!