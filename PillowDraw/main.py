# example taken from :
# http://pillow.readthedocs.org/en/latest/reference/ImageDraw.html

import sys

from PIL import Image, ImageDraw

im = Image.open("img.jpg")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128, width=10)
draw.line((0, im.size[1], im.size[0], 0), fill=128, width=5)
del draw

im.save("outfile.png", "PNG")
