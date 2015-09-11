#!/usr/bin/env python

# read the doc about sharpening:
# http://pillow.readthedocs.org/en/latest/reference/ImageFilter.html

import os
import sys
from PIL import Image
from PIL import ImageFilter

# Loop through all provided arguments
for i in range(1, len(sys.argv)):
    try:
        # Attempt to open an image file
        filepath = sys.argv[i]
        image = Image.open(filepath)
    except IOError, e:
        # Report error, and then skip to the next argument
        print "Problem opening", filepath, ":", e
        continue

    # Perform operations on the image here

    # Sharpen
    image = image.filter(ImageFilter.SHARPEN)
    #image = image.filter(ImageFilter.DETAIL)

    # Split our original filename into name and extension
    (name, extension) = os.path.splitext(filepath)

    # Save with "_changed" added to the filename
    image.save(name + '_changed' + extension)

    # Save the image as a JPG
    image.save(name + '.jpg')
