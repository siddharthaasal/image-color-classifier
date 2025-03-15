import cv2
import os
import shutil

# Define folders
data_folder = "./data"
colored_folder = "./colored"
grayed_folder = "./grayed"

# Ensure output folders exist
os.makedirs(colored_folder, exist_ok=True)
os.makedirs(grayed_folder, exist_ok=True)

# Iterate over images in the data folder
for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)
    
    # Read the image
    image = cv2.imread(file_path)
    
    # Skip if the file is not a valid image
    if image is None:
        continue
    
    # Check if image is grayscale or colored
    is_colored = False
    for row in image:
        for pixel in row:
            if pixel[0] != pixel[1] or pixel[1] != pixel[2]:
                is_colored = True
                break
        if is_colored:
            break
    
    # Move the image to the appropriate folder
    if is_colored:
        shutil.move(file_path, os.path.join(colored_folder, filename))
    else:
        shutil.move(file_path, os.path.join(grayed_folder, filename))

print("Processing complete.")
