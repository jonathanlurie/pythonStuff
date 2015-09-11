# download tile from OSM/mapbox, like the old poster maker! (but better)
# for Mapbox access : https://www.mapbox.com/developers/api/maps/
# for static maps : https://www.mapbox.com/developers/api/static/

# mergin de tuiles avec Imagemagick : http://www.imagemagick.org/Usage/crop/#crop_tile


from TheGrowingBox import *

class TileHandler:

    # bounding box coodinates (decimal wgs84)
    _boxW = None
    _boxS = None
    _boxE = None
    _boxN = None

    # linked to dpi.
    # 1 for standard
    # 2 for retina
    _resolutionFactor = 2

    # skin used to customize the tiles
    _skin = "/Users/jonathanlurie/Documents/code/gitRepo/mapboxStudioSkins/highcontrast.tm2"


    # download tiling
    _maxTileSide = 1024
    _latNbTiles = 2
    _lonNbTiles = 2


    # folders
    _temporaryFolder = "temp"
    _outputFolder = "output"


    def __init__(self):
        None

    # Mandatory
    # set the bounding box in decimal wgs84
    def setGeoBox(w, s, e, n):
        self._boxW = w
        self._boxS = s
        self._boxE = e
        self._boxN = n


    # Optional
    # set the resoltion factor (1 : normal, 2 : retina, etc.)
    def setResolutionFactor(f):
        self._resolutionFactor = f



    def setSkin(s):
        self._skin = s


    # see doc:
    # http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_2
    def deg2num(lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0 ** zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
        return (xtile, ytile)


    def num2deg(xtile, ytile, zoom):
        n = 2.0 ** zoom
        lon_deg = xtile / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
        lat_deg = math.degrees(lat_rad)
        return (lat_deg, lon_deg)
