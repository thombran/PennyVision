import imageio
import math

def main():
    cropped_read = imageio.imread('./pennyCropped.jpg') # Loading in image data
    data_crop = [[0 for x in range(cropped_read.shape[1])] for y in range(cropped_read.shape[0])] # Instantiating empty matrix for values
    # Iterate through rows and columns of image data_crop and create a data_crop point corresponding to greyscale value
    for row in range(0, cropped_read.shape[0]):
        for col in range(0, cropped_read.shape[1]):
            # Weighted greyscale calculatuon
            data_crop[row][col] = cropped_read[row, col, 0] * .299 + cropped_read[row, col, 1] * .587 + cropped_read[row, col, 2] * .114 
    
    full_read = imageio.imread('./pennyFull.jpeg') # Load in image data for full image
    data_full = [[0 for x in range(full_read.shape[1])] for y in range(full_read.shape[0])]
    # Convert full image to greyscale values, push to data_full matrix
    for row in range(0, full_read.shape[0]):
        for col in range(0, full_read.shape[1]):
            data_full[row][col] = full_read[row, col, 0] * .299 + full_read[row, col, 1] * .587 + full_read[row, col, 2] * .114 

    euclidean_data = [[0 for x in range(full_read.shape[1])] for y in range(full_read.shape[0])]
    row = 0
    col = 0
    while(row != full_read.shape[0]):
        while(col != full_read.shape[1]):
            

main()
