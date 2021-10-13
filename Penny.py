import imageio
import matplotlib.pyplot as plt
import math

def main():
    cropped_read = imageio.imread('./PennyCropNew.jpg') # Loading in image data
    data_crop = [[0 for x in range(cropped_read.shape[1])] for y in range(cropped_read.shape[0])] # Instantiating empty matrix for values
    # Iterate through rows and columns of image data_crop and create a data_crop point corresponding to greyscale value
    for row in range(0, cropped_read.shape[0]):
        for col in range(0, cropped_read.shape[1]):
            # Weighted greyscale calculatuon
            data_crop[row][col] = cropped_read[row, col, 0] * .299 + cropped_read[row, col, 1] * .587 + cropped_read[row, col, 2] * .114

    full_read = imageio.imread('./PennyInNew.jpg') # Load in image data for full image
    data_full = [[0 for x in range(full_read.shape[1])] for y in range(full_read.shape[0])]
    # Convert full image to greyscale values, push to data_full matrix
    for row in range(0, full_read.shape[0]):
        for col in range(0, full_read.shape[1]):
            data_full[row][col] = full_read[row, col, 0] * .299 + full_read[row, col, 1] * .587 + full_read[row, col, 2] * .114

    full_img = plt.imshow(data_full)
    plt.show()

    e_rows = full_read.shape[0] - cropped_read.shape[0]
    e_cols = full_read.shape[1] - cropped_read.shape[1]
    t_rows = cropped_read.shape[0]
    t_cols = cropped_read.shape[1]
    print(e_rows)
    print(e_cols)
    print(t_rows)
    print(t_cols)

    euclidean_data = [[0 for x in range(0, e_cols)] for y in range(0, e_rows)]
    print('data created')
    for i in range(0, e_rows):
        for j in range(0, e_cols):
            for k in range(0, t_rows):
                for l in range(0, t_cols):
                    euclidean_data[i][j] += abs(data_full[i+k][j+l] - data_crop[k][l])

main()
