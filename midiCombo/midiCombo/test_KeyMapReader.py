"""
Test reading a mapping file containing keyboard simulation instructions.
Parse the file, put keys and arguments in a map.

NOTE: some text editor are replacing tabs by spaces, which is not good for
MappingItem.

"""


from KeyMapReader import *

kmr = KeyMapReader()

# setting the file address
kmr.setMapFileName("/Users/jonathanlurie/Documents/code/pythonStuff/midiCombo/midiCombo/input/config.map")

# process the mapping file
kmr.processMapFile()

# getting the mapping configuration as a python map container
theMappingMap = kmr.getKeyArgumentMap()


print(theMappingMap)
