from PIL import Image
import sys
import os
import glob


class TileMerger:

	def __init__(self):
		# number of tiles in line
		self.nbXtiles = None

		# number of tiles in column
		self.nbYtiles = None

		# directory to find the tile
		self.tileDirectory = None

		# directory where the final big image will be exported
		self.outputDirectory = None

		# tile extention
		self.tileExtention = ".jpg"

		# default size of a tile
		self.defaultTileSize = 640

		# title of the final image
		self.title = "Untitled"

		# output object image
		self.outputImage = None
		
		# the margin size between images (no outer) in pixel
		self.marginSize = 0
		
		# margin color, white by default
		self.marginColor = "#FFFFFF"

	def setNbXtiles(self, nb):
		self.nbXtiles = nb

	def setNbYtiles(self, nb):
		self.nbYtiles = nb

	def setTileDirectory(self, dire):
		self.tileDirectory = dire
		self.outputDirectory = dire

	def setOutputDirectory(self, dire):
		self.outputDirectory = dire

	def setTileExtention(self, extent):
		self.tileExtention = extent

	def setDefaultTileSize(self, s):
		self.setDefaultTileSize = s

	def setTitle(self, t):
		self.title = t
		
	def setMarginSize(self, s):
		self.marginSize = s
		
	# set te margin color as an hexadecimal value string "#FF00FF"
	def setMarginColor(self, c):
		self.marginColor = c

	def mergeTilesAndExport(self):
		# check the output directory, if doesnt exist, we create it
		if(not os.path.isdir(self.outputDirectory)):
			os.makedirs(self.outputDirectory)

			
		
		# creation of the empty big output image
		self.outputImage = Image.new("RGB", (self.defaultTileSize*self.nbXtiles + (self.marginSize)*(self.nbXtiles - 1), self.defaultTileSize*self.nbYtiles + (self.marginSize)*(self.nbYtiles - 1)) , self.marginColor)
		
		maxTiles = self.nbXtiles * self.nbYtiles
		
		# gloging the image filename
		allImages = glob.glob(self.tileDirectory + "/*" +  self.tileExtention)
		
		if(len(allImages) < (self.nbYtiles*self.nbXtiles)):
			print(   "WARNING: " + str(self.nbYtiles*self.nbXtiles)  + " tiles are required, only " + str(len(allImages)) + " are provided." )
			#return
		
		itTile = 0
		
		for x in range(0, self.nbXtiles):
			for y in range(0, self.nbYtiles):
			
				if(itTile >= len(allImages)):
					break
			
				#currentTileName = self.tileDirectory + "/" + str(x) + "_" + str(y) + "_" + self.tileExtention
				currentTileName = allImages[itTile]
				
				# test if this current tile exists
				if(os.path.isfile(currentTileName)):
					#print(currentTileName)
					tempTile = Image.open(currentTileName)
					
					print("merge tuile " + str(itTile+1) + "/" + str(maxTiles))
					itTile += 1
					# adding the tile content to the big output image
					self.outputImage.paste(tempTile, (x*self.defaultTileSize + x*self.marginSize, y*self.defaultTileSize + y*self.marginSize))
				
				
				
					
				else:
					print("ERROR: la tuile attendue " + currentTileName + " n'existe pas.")
					return
					
					
				
			
		# finally export the tile
		finalName = self.outputDirectory + "/" + self.title + ".jpg"
		
		self.outputImage.save(finalName, "JPEG")
		print("INFO: image finale exportee ici: " + finalName)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		