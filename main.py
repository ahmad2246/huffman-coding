# -*- coding: utf-8 -*-

import cv2
import numpy as np
from skimage import metrics
import os
import time
from huffman import HuffmanEncoding, HuffmanDecoding

# Stating the time
start_time = time.time()

# Load the image here
image_path = 'r02b3a1ddt.tif'

img = cv2.imread(image_path)

# Flatten the image into a 1D array
pixel_values_array = img.ravel()

pixel_values = pixel_values_array.tolist()  

encoded_output, the_tree = HuffmanEncoding(pixel_values)

Decoded_Output = np.array(HuffmanDecoding(encoded_output, the_tree))

# Reshape the pixel values back into the original shape of the image
restored_img = Decoded_Output.reshape(img.shape)

# Save the restored image as "restored.png"
saved_image_path = 'restored.png'
cv2.imwrite(saved_image_path, restored_img)
print("restored image has been saved as: ", saved_image_path)

# Checking if the hufman coding is doing Lossless compression
are_arrays_equal = np.array_equal(pixel_values_array, Decoded_Output)
if are_arrays_equal:
    print("This huffman coding code is doing a Lossless compression")
else:
    print("This huffman coding code is not doing a Lossless compression")
    
#---------------------
# image quality metrics
#---------------------

# get the size of the images
refference_size = os.path.getsize(image_path)
restored_size = os.path.getsize(saved_image_path)

# Calculate the compression ratio
compression_ratio = refference_size / restored_size
print('Compression Ratio:', compression_ratio)

# Calculate mse
mse = metrics.mean_squared_error(img, restored_img)
print("mse:", mse)

# Calculate PSNR
if mse != 0:
    psnr = metrics.peak_signal_noise_ratio(img, restored_img, data_range=None)
    print("PSNR:", psnr)
else:
    print("PSNR: infinity")

#---------------------
# end
#---------------------

end_time = time.time()
total_time = end_time - start_time

print(f"Total time taken: {total_time} seconds")