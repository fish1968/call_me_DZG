import cv2
import os

folder_path = './'  # Path to the folder containing the images

# Specify the coordinates of the point
x = 52
y = 50

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (you may need to adjust the file extensions)
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Load the image
        image = cv2.imread(file_path)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Access the pixel value at the specified point
        brightness = gray_image[y, x]
        # Calculate the average brightness of the image
        # brightness = gray_image.mean()
        

        print(f"Brightness of {filename}: {brightness}")
