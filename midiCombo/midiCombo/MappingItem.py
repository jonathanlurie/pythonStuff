# a mapping item is an association between 3 things:
# a FIGURE is the MIDI key index,
# a STATE is P for pressed or R for released,
# a ARGUMENT is the keyboard mapping key

import re

class MappingItem:

	m_originalString = None
	m_mapKey = None
	m_mapArgument = None
	m_isValid = False

	def __init__(self, theOrigString):
		self.m_originalString = theOrigString
		self.checkIntegrity()

	def getMapKey(self):
		return self.m_mapKey;

	def getMapAgument(self):
		return self.m_mapArgument;

	def checkIntegrity(self):
		# use split('\t') instead, in order to be able to use space character in the argument part (last)
		tempArray = self.m_originalString.split('\t')

		# 1st condition: there must be 4 elements in the array
		if(len(tempArray) == 3):

			# 2nd condition: the second must be a digit
			if(tempArray[0].isdigit()):
				self.m_columnIndex = int(tempArray[0])

				# 3rd condition: the 3rd element must be P, p, R, or r
				if( re.match("^[PpRr]*$", tempArray[1]) and len(tempArray[1]) == 1  ):
					self.m_mapKey = str(tempArray[0]) + str(tempArray[1]).upper()
					self.m_mapArgument = tempArray[2]
					self.m_isValid = True

	def printInfo(self):
		if(self.m_isValid):
			print("Original string: " + self.m_originalString)
			print("Map argument: " + self.m_mapArgument)
			print("Map key: " + self.m_mapKey)
		else:
			print("ERROR: the string is invalid, info cannot be printed.")

	def isValid(self):
		return self.m_isValid
