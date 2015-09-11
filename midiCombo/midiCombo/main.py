

# data container
from collections import Counter


# project imports
from KeyMapReader import *
from MidiDeviceReader import *
from CommandInterpreter import *



try:
    # creating the key map reader, in charge of reading the
    # instruction from the .setting file
    kmr = KeyMapReader()
    kmr.setMapFileName("input/config.map")
    kmr.processMapFile()

    # creating the command interpreter
    ci = CommandInterpreter()
    # giving the key-argument map to the command interpreter:
    ci.setKeyArgumentMap(  kmr.getKeyArgumentMap() )



    mdr = MidiDeviceReader()
    mdr.setCommandInterpreter(ci)
    mdr.readFlow()

    # creating the serial matrix reader, in charge of catching
    # the messages from the tangible matrix
    #smr = SerialMatrixReader()
    #smr.setCommandInterpreter(ci)
    #smr.readFlow()

except KeyboardInterrupt:
    mdr.close()
    exit()
