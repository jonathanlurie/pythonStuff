'''
based on this tutorial
http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php

'''

import cv2
import numpy as np


# loading an image in a numpy.ndarray data structure
img = cv2.imread('images/_NIK7651.JPG')

# accessing some informations
print img.shape # array (height, width, nb chanels)
print img.dtype # uint8
print img.size  # number of pix = w*h


# accessing a pixel value
print img[10, 16]


# read a second image
img2 = cv2.imread('images/_NIK7652.JPG')

# make an iverage image
img3 = img2/2 + img/2


# save it
cv2.imwrite('out.tif',img3)
