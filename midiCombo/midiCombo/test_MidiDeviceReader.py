
from MidiDeviceReader import *


myDevice = MidiDeviceReader("LPK25")
myDevice.readFlow()

# si la methode close n'a pas ete appellee en interne, il faut l'appeller!!
myDevice.close()
