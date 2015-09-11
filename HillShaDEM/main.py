from PIL import Image
import math

#imgAddress = "/Users/jonathanlurie/Documents/images/DEM/test01.jpg"
#imgAddress = "/Users/jonathanlurie/Documents/images/DEM/demReal.jpg"
#imgAddress = "/Users/jonathanlurie/Documents/images/DEM/test02.png"
imgAddress = "/Users/jonathanlurie/Documents/images/DEM/FilledDEM.jpg"

im = Image.open(imgAddress)
rgb_im = im.convert('RGB')



#print(im.format, im.size, im.mode)
#im.show()

# output image
outputData = Image.new("RGB", im.size , 0)

for x in range(0+1, im.size[0]-1):
    for y in range(0+1, im.size[1]-1):

        rIn, gIn, bIn = rgb_im.getpixel((x, y))
        rInEast, gInEast, bInEast = rgb_im.getpixel((x+1, y))
        rInSouth, gInSouth, bInSouth = rgb_im.getpixel((x, y+1))

        rInWest, gInWest, bInWest = rgb_im.getpixel((x-1, y))
        rInNorth, gInNorth, bInNorth = rgb_im.getpixel((x, y-1))


        # TODO : caculer l'angle depuis les diagonales aussi, puis faire une moyenne
        # apres l'avoir rectifier de 45 degres.


        denom = rInWest-rInEast
        if(denom == 0):
            denom = math.pi

        angle =  (   math.atan((float(rInNorth-rInSouth))/(float(denom)))   + math.pi/2.) / math.pi * 180.

        outputData.putpixel((x, y), (int(angle), int(angle), int(angle) ))




outputData.show()
