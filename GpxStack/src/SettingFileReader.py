from ConfigParser import *


class SettingFileReader:

    _fileName = 'settings.ini'
    _parser = None

    def __init__(self):
        self._parser = SafeConfigParser()
        self._parser.read(self._fileName)

    # returns True if the geo bounding box is automatically estimated
    def getAutoGeoBox(self):
        try:
            if( int(self._parser.get('geobox', 'auto')) == 1 ):
                return True
            else:
                return False
        except NoOptionError as e:
            print e
            return False


    # Return the north border coordinate, in decimal format
    def getNorthBorder(self):
        try:
            return float(self._parser.get('geobox', 'north'))
        except NoOptionError as e:
            print e
            return None


    # Return the south border coordinate, in decimal format
    def getSouthBorder(self):
        try:
            return float(self._parser.get('geobox', 'south'))
        except NoOptionError as e:
            print e
            return None


    # Return the west border coordinate, in decimal format
    def getWestBorder(self):
        try:
            return float(self._parser.get('geobox', 'west'))
        except NoOptionError as e:
            print e
            return None


    # Return the east border coordinate, in decimal format
    def getEastBorder(self):
        try:
            return float(self._parser.get('geobox', 'east'))
        except NoOptionError as e:
            print e
            return None

    # return the number of pixel per degree on the final image
    def getPixelPerDegree(self):
        try:
            return float(self._parser.get('geobox', 'pixelPerDegree'))
        except NoOptionError as e:
            print e
            return None

    # returns the stroke weight used for drawing the image
    def getStrokeWidth(self):
        try:
            return float(self._parser.get('graphic', 'strokeWidth'))
        except NoOptionError as e:
            print e
            return 1


    # returns the stroke color as an array of size 3
    def getStrokeColor(self):
        try:
            colorStr = self._parser.get('graphic', 'strokeColor')
            colorArray = colorStr.split(',')
            colorArrayInt = []
            for c in colorArray:
                colorArrayInt.append(float(c)/255.)

            return colorArrayInt

        except NoOptionError as e:
            print e
            return [1, 0, 0]


    # returns the background color as an array of size 3
    def getBackgroundColor(self):
        try:
            colorStr = self._parser.get('graphic', 'backgroundColor')
            colorArray = colorStr.split(',')
            colorArrayInt = []
            for c in colorArray:
                colorArrayInt.append(float(c)/255.)

            return colorArrayInt

        except NoOptionError as e:
            print e
            return [1, 0, 0]
