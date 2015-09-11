'''
BLANK_PY
=============
Copyright (c) 2015, Jonathan LURIE, All rights reserved.
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with this library.
'''

import os
from SettingFileReader import *

from ctypes import cdll
from ctypes import c_char_p
exiv2wrapperLib = cdll.LoadLibrary("libexiv2wrapper.dylib")



def getXmpValue():

    getXmpValueFn = exiv2wrapperLib.getXmpValue
    getXmpValueFn.restype = c_char_p

    print getXmpValueFn("/Users/jonathanlurie/Desktop/_NIK4337.xmp", "Xmp.crs.Highlights2012")


def addXmpStrField():
    addXmpFiedlFn = exiv2wrapperLib.addXmpStrField
    print addXmpFiedlFn("/Users/jonathanlurie/Desktop/_NIK4337.xmp", "Xmp.crs.leChampPerso", "la Valeur")

def addXmpSeqField():
    addXmpSeqFieldFn = exiv2wrapperLib.addXmpSeqField
    sequence = "elem1|elem2|elem3"
    print addXmpSeqFieldFn("/Users/jonathanlurie/Desktop/_NIK4337.xmp", "Xmp.crs.laSequence", sequence)

def deleteXmpField():
    delXmpFieldFn = exiv2wrapperLib.









    print delXmpFieldFn("/Users/jonathanlurie/Desktop/_NIK4337.xmp", "Xmp.crs.laSequenceMMM")


# main
if __name__ == '__main__':

    # cleaning terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n------------------------ BLANK_PY -----------------------------------------\n")

    '''
    # loading a setting from the setting file
    settings = SettingFileReader()
    someSetting = settings.getSetting("group2", "param1")
    print(someSetting)

    # you want to update a param in the setting.ini file? no problem
    settings.setSetting("group2", "param3", "leParam3")
    '''

    # OK
    #getXmpValue()

    # OK
    #addXmpStrField()

    # OK
    #addXmpSeqField()

    # mm
    #deleteXmpField()
