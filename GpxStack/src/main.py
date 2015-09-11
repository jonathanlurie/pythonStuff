'''
GpxStack
=============
Copyright (c) 2015, Jonathan LURIE, All rights reserved.
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with this library.
'''

import os
import math
from SettingFileReader import *
from Geographic import *


# main
if __name__ == '__main__':

    # cleaning terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n------------------------ GpxStack -----------------------------------------\n")

    settings = SettingFileReader()

    print settings.getAutoGeoBox()
    print settings.getNorthBorder()
    print settings.getSouthBorder()
    print settings.getWestBorder()
    print settings.getEastBorder()
    print settings.getPixelPerDegree()

    print settings.getStrokeWidth()
    print settings.getStrokeColor()



    geox = Geographic()
    geox.setGpxFile("")
    geox.guessBoundingBox()
    geox.printGeoBox()
    geox.computeOutputImageSize(settings.getPixelPerDegree())
    print("\n")
    geox.printOutputImageSize()
    print("\n")

    #allSegments = geox.preparePolylines()
    allSegments = geox.preparePolylinesTuples()



    # --------------- to put in a clasee!


    # TODO : replace this part by a Pillow usage!

    from PIL import Image
    from PIL import ImageDraw

    surface = Image.new("RGB", (int(geox.getImageWidth()) +1, int(geox.getImageHeight())+1 ) ,"#FFFFFF")

    draw = ImageDraw.Draw(surface)

    for segment in allSegments:
        draw.line(segment, fill=128, width=10)


    #allSegmentsInOneTrack = geox.preparePolylinesTuplesOneTrack()
    #draw.line(allSegmentsInOneTrack, fill=128, width=10)

    del draw

    surface.save("outfile.png", "PNG")
