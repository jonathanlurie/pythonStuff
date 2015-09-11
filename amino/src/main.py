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

import sys
import os
from SettingFileReader import *

import translate
import Utils


def formatString(base, amino):

    # number of aminoacid to display by line
    numberOfAAToDisplay = 30
    numberOfCharByLine = numberOfAAToDisplay * 3

    numberOfLines = ( len(amino)/3 ) / numberOfAAToDisplay

    if(( len(amino)/3 ) % numberOfAAToDisplay):
        numberOfLines = numberOfLines + 1

    print "number of base : " + str(len(base))
    print "number of aa : " + str(len(amino)/3)


    for l in range(0, numberOfLines):
        firstLine = base[l*numberOfCharByLine: (l+1)*numberOfCharByLine]
        secondLine = amino[l*numberOfCharByLine: (l+1)*numberOfCharByLine]

        print firstLine
        print secondLine
        print ""




# main
if __name__ == '__main__':

    # gives priority to local libs
    sys.path.insert(0, "./lib/python")

    # cleaning terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n------------------------ AMINO -----------------------------------------\n")

    nucleoBaseSequenceFile = "data/huntingtin.seq"
    #sequenceFile = "data/Untitled.txt"

    nucleoBaseSequence = Utils.loadTextFile(nucleoBaseSequenceFile)
    nucleoBaseSequence = nucleoBaseSequence.replace("\n", "")

    aminoSequence = translate.translate(nucleoBaseSequence)

    formatString(nucleoBaseSequence, aminoSequence)
