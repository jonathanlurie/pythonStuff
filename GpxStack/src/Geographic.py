import gpxpy
import gpxpy.gpx

class Geographic:

    _gpxFile = None
    _gpxObject = None

    _north = None
    _south = None
    _west = None
    _east = None

    _imageWidth = None
    _imageHeight = None


    def __init__(self):
        print("")

    # set the gpx file address, then reads it
    def setGpxFile(self, f):
        #self._gpxFile = open('data/toulouse1.gpx', 'r')
        self._gpxFile = open('data/Rochefort.gpx', 'r')
        self._gpxObject = gpxpy.parse(self._gpxFile)


    # set the bounding box coordinate
    def setGeoBoxNSEW(self, n, s, e, w):
        self._north = n
        self._south = s
        self._west = w
        self._east = e


    # using the gpx file, takes the min and for lat and lon
    def guessBoundingBox(self):

        for track in self._gpxObject.tracks:
            for segment in track.segments:
                for point in segment.points:
                    #print 'Point at ({0},{1})'.format(point.latitude, point.longitude)

                    if(self._south == None or self._south > point.latitude):
                        self._south = point.latitude

                    if(self._west == None or self._west > point.longitude):
                        self._west = point.longitude


                    if(self._north == None or self._north < point.latitude):
                        self._north = point.latitude

                    if(self._east == None or self._east < point.longitude):
                        self._east = point.longitude


            # TODO: enlarge 10%
            latMargin = abs(self._south - self._north) * 0.05
            lonMargin = abs(self._west - self._east) * 0.05

            self._south = self._south - latMargin
            self._north = self._north + latMargin
            self._east = self._east + lonMargin
            self._west = self._west - lonMargin


    # print on screen
    def printGeoBox(self):
        print("\nGeoBox:")
        print('lat ({0},{1}) Delta: {2}'.format(self._south, self._north, self._north-self._south))
        print('lon ({0},{1}) Delta: {2}'.format(self._west, self._east, self._east-self._west))


    # return the geobox as an array
    def getGeoBoxNSEW(self):
        return [self._north, self._south, self._east, self._west]


    # compute the output image size in pixel
    def computeOutputImageSize(self, pixelPerDegree):

            self._imageWidth = abs(self._east-self._west) * float(pixelPerDegree)
            self._imageHeight = abs(self._north-self._south) * float(pixelPerDegree)


    def getImageWidth(self):
        return self._imageWidth

    def getImageHeight(self):
        return self._imageHeight

    # just a print
    def printOutputImageSize(self):
            print("width: " + str(self._imageWidth))
            print("height: " + str(self._imageHeight))


    # return image coordinate from gps coordinates
    def getImageCoordinates(self, gpsLatLon):

        # if at NORTH
        if(gpsLatLon[0] > 0):
            # remember the 0,0 in an image is at TOP-LEFT !!!
            imgLat = float(self._imageHeight) - ( abs(gpsLatLon[0] - self._south) / abs(self._north - self._south) * float(self._imageHeight))

        # if at SOUTH
        # TODO : to test
        else:
            imgLat = abs(gpsLatLon[0] - self._north) / abs(self._south - self._north) * float(self._imageHeight)


        # if at EAST !!
        if(gpsLatLon[1] > 0):
            imgLon = abs(gpsLatLon[1] - self._west ) / abs(self._east - self._west) * float(self._imageWidth)

        # if at WEST !!
        # TODO : to test
        else:
            imgLon =  float(self._imageWidth) - ( abs(gpsLatLon[1] - self._east) / abs( self._east - self._west) * float(self._imageWidth))

        # imgLat is Y because "ALONG" the lat, same thing with imgLon
        return [imgLon, imgLat]


    def preparePolylines(self):

        allSegments = []

        currentSegment = []

        for track in self._gpxObject.tracks:
            for segment in track.segments:
                for point in segment.points:
                    #print 'Point at ({0},{1})'.format(point.latitude, point.longitude)

                    currentSegment.append(self.getImageCoordinates([point.latitude, point.longitude]))

                allSegments.append(currentSegment)


        return allSegments




    def preparePolylinesTuples(self):

        allSegments = []

        currentSegment = ()

        for track in self._gpxObject.tracks:
            for segment in track.segments:
                for point in segment.points:
                    #print 'Point at ({0},{1})'.format(point.latitude, point.longitude)

                    #currentSegment.append(self.getImageCoordinates([point.latitude, point.longitude]))

                    coordAsArray = self.getImageCoordinates([point.latitude, point.longitude])

                    currentSegment = currentSegment + (coordAsArray[0], coordAsArray[1])

                allSegments.append(currentSegment)


        return allSegments



    def preparePolylinesTuplesOneTrack(self):

        allSegments = ()



        for track in self._gpxObject.tracks:
            for segment in track.segments:
                for point in segment.points:
                    #print 'Point at ({0},{1})'.format(point.latitude, point.longitude)

                    #currentSegment.append(self.getImageCoordinates([point.latitude, point.longitude]))

                    coordAsArray = self.getImageCoordinates([point.latitude, point.longitude])

                    allSegments = allSegments + (coordAsArray[0], coordAsArray[1])



        return allSegments
