"""
Test the MappinItem class (unit test).

"""

from MappingItem import *

# the string to test.
# must be splited into 3 parts:
#   - A number for key index
#   - a letter from {P p R r} for press or release
#   - a string argument
aValidInput = "1\tP\tplugin|keyboard|typeString|hello"

aValidInput2 = "19\tP\tplugin|keyboard|typeString|hello"

aInvalidInput = "19\tM\tplugin|keyboard|typeString|hello"

aInvalidInput2 = "19\tM\tword\tplugin|keyboard|typeString|hello"

mi = MappingItem(aInvalidInput2)
print("isValid: " + str(mi.isValid()))
mi.printInfo()
