import sys
from TileMerger import *



# input tile folder 
inputTileFolder = "D:\\Dropbox\\Instagram\\likes"
#inputTileFolder = "D:\\projets\\code\\autres\\python\\instaMerge\\test\\input"


merger = TileMerger()
merger.setNbXtiles(24)
merger.setNbYtiles(34)
merger.setMarginColor("#FFFFFF")
merger.setMarginSize(0)
merger.setTileExtention(".jpg")
merger.setTileDirectory(inputTileFolder)
merger.setOutputDirectory("D:\\projets\\code\\autres\\python\\instaMerge\\test\\output")
merger.setTitle("instaMergeNoMargin")
merger.mergeTilesAndExport()

os.system("pause")
