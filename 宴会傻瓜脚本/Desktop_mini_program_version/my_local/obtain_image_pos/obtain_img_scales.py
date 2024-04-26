import os
import csv
from PIL import Image

def scan_images(folder_path, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Height', 'Width'])

        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    try:
                        with Image.open(file_path) as img:
                            width, height = img.size
                            writer.writerow([file_name, height, width])
                    except (IOError, OSError):
                        print("Failed to process image: {}".format(file_name))

# Set the folder path to scan the current directory
folder_path = './'

# Provide the CSV file path to export the data
csv_file = './output.csv'

scan_images(folder_path, csv_file)

#import os
#from PIL import Image

#def scan_images(folder_path):
#    for root, dirs, files in os.walk(folder_path):
#        for file_name in files:
#            file_path = os.path.join(root, file_name)
#            if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
#                try:
#                    with Image.open(file_path) as img:
#                        width, height = img.size
#                        print("Name: {}\nHeight: {} pixels\nWidth: {} pixels\n".format(file_name, height, width))
#                except (IOError, OSError):
#                    print("Failed to process image: {}".format(file_name))

# Provide the folder path you want to scan
#folder_path = './'

#scan_images(folder_path)