import imageio
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
import os

# Authors: Daniel Floyd & Brandon Thomas
# CIS 365 - Professor Denton Bobeldyk
# 10/13/2021
# Assignment Six - AI Vision
# This Python program takes in an image as the argument and searches the image for a penny. Found pennies can be visually
# seen at the end in the image as a dark spot. For the purposes of this assignment, both an image with and without a penny
# will be used. One can be seen with a dark spot towards the middle of the image, the other does not have this spot. 

if len(sys.argv) != 2:
    print('Please supply an image file\nUsage: python penny.py example.jpg')
    exit(1)

image = sys.argv[1]
if not os.path.exists(image):
    print('Image file is invalid')
    exit(1)

cropped_read = imageio.imread('./PennyCropNew.jpg') # Loading in image data
data_crop = [[0 for x in range(cropped_read.shape[1])] for y in range(cropped_read.shape[0])] # Instantiating empty matrix for values
# Iterate through rows and columns of image data_crop and create a data_crop point corresponding to greyscale value
for row in range(0, cropped_read.shape[0]):
    for col in range(0, cropped_read.shape[1]):
        # Weighted greyscale calculation
        data_crop[row][col] = cropped_read[row, col, 0] * .299 + cropped_read[row, col, 1] * .587 + cropped_read[row, col, 2] * .114

full_read = imageio.imread(image) # Load in image data for full image
data_full = [[0 for x in range(full_read.shape[1])] for y in range(full_read.shape[0])]
# Convert full image to greyscale values, push to data_full matrix
for row in range(0, full_read.shape[0]):
    for col in range(0, full_read.shape[1]):
        data_full[row][col] = full_read[row, col, 0] * .299 + full_read[row, col, 1] * .587 + full_read[row, col, 2] * .114

full_image_rows = full_read.shape[0] - cropped_read.shape[0]
full_image_cols = full_read.shape[1] - cropped_read.shape[1]
cropped_image_rows = cropped_read.shape[0]
cropped_image_cols = cropped_read.shape[1]

#fill array with 0s
euclidean_data = [[0 for x in range(0, full_image_cols)] for y in range(0, full_image_rows)]
for i in tqdm(range(0, full_image_rows), desc="Calculating", ascii=False, ncols=76):
    for j in range(0, full_image_cols):
        for k in range(0, cropped_image_rows):
            for l in range(0, cropped_image_cols):
                euclidean_data[i][j] += abs(data_full[i+k][j+l] - data_crop[k][l])
print('Complete.')

full_img = plt.imshow(euclidean_data)
plt.show()