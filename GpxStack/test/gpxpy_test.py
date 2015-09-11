import gpxpy
import gpxpy.gpx

# for elevation correction
import srtm

# Parsing an existing file:
# -------------------------

gpx_file = open('data/toulouse1.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

elevation_data = srtm.get_data()

# setting the box:
minLat = None
maxLat = None
minLon = None
maxLon = None
minAlt = None
maxAlt = None


for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print 'Point at ({0},{1})'.format(point.latitude, point.longitude)

            if(minLat == None or minLat > point.latitude):
                minLat = point.latitude

            if(minLon == None or minLon > point.longitude):
                minLon = point.longitude

            if(minAlt == None or minAlt > elevation_data.get_elevation(point.latitude, point.longitude)):
                minAlt = elevation_data.get_elevation(point.latitude, point.longitude)


            if(maxLat == None or maxLat < point.latitude):
                maxLat = point.latitude

            if(maxLon == None or maxLon < point.longitude):
                maxLon = point.longitude

            if(maxAlt == None or maxAlt < elevation_data.get_elevation(point.latitude, point.longitude)):
                maxAlt = elevation_data.get_elevation(point.latitude, point.longitude)


print("\nGeoBox:")
print('lat ({0},{1}) Delta: {2}'.format(minLat, maxLat, maxLat-minLat))
print('lon ({0},{1}) Delta: {2}'.format(minLon, maxLon, maxLon-minLon))
print('alt ({0},{1}) Delta: {2}'.format(minAlt, maxAlt,  maxAlt-minAlt))
