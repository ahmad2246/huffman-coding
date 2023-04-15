# Huffman Image Compression

This program uses Huffman coding for lossless image compression. It utilizes a modified version of the "huffman" code from the website "https://www.javatpoint.com/huffman-coding-using-python" and requires several libraries, including cv2, numpy, skimage.metrics, os, and time.

To compress an image, the program first reads it using cv2.imread and then applies Huffman coding. The resulting compressed binary file is saved to disk.

Afterwards, the compressed binary file is read and decoded using Huffman decoding, and the original image is reconstructed and saved. Finally, the program performs some image quality metrics.

It's worth noting that the compressed binary file size may be larger than expected because each bit of the encoded message is stored as a separate character in a text file, which requires eight times as much storage as the bitstream. To fix this, the OutputEncoded() function in the huffman.py module can be modified to open the file in binary mode and write the bitstream directly to it using the write() method, converting the bitstream into bytes by dividing it into chunks of 8 bits and using the bytes() function.




## Brief introduction about Huffman coding

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to individual symbols based on their frequency of occurrence in the input data. The more frequently a symbol occurs, the shorter its corresponding code. Conversely, less frequent symbols are assigned longer codes.

The algorithm works by first constructing a binary tree based on the frequency of each symbol in the input data. Each leaf node of the tree represents a symbol, and its corresponding code is determined by traversing the tree from the root to the leaf node. Codes are assigned to the left branch as "0" and to the right branch as "1". The codes for each symbol are then determined by the path from the root of the tree to the corresponding leaf node.

This results in a prefix-free code, which means that no code for any symbol is a prefix of the code for any other symbol. This property ensures that the original data can be uniquely decoded from the compressed data, and the compression is lossless. The resulting compressed data can be stored more efficiently, as shorter codes are used for more frequent symbols, resulting in a more compact representation of the input data.



## Requirements

* numpy
* skimage
* cv2
* os
* time

## Installation

Install the required libraries by running:

```
pip install numpy
pip install scikit-image
pip install opencv-python
```

### Usage

* Download or clone this repository.
* Place the image you want to compress in the same directory as the Huffman.py file.
* Change the image_path variable in the compress.py file to the name of your image file
* change the saved_image_path variable in the compress.py file to the name of your recounstraced image file
* Run Huffman.py.
* The compressed binary file will be saved in the same directory as 'encoded_file.bin'.


### Side notes

The size of the recounstraced image should be almost identical to the original image when saving it in a png format
and hence:

* mse = 0
* psnr = infinity

Which indicates that this is a Lossless compression
