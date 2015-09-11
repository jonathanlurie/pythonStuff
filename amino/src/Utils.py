import os
from ctypes import cdll
import time
import datetime

# return the basename of a file, without its extension
def getBasenameNoExt(wholeAddress):
    return os.path.splitext(os.path.basename(wholeAddress))[0]

# return the basename of a file, without its extension
def getBasenameWithExt(wholeAddress):
    return os.path.basename(wholeAddress)

# just a dirname
def getFolderName(wholeAddress):
    return os.path.dirname(wholeAddress)

# return the extension of a file
def getFileExt(wholeAddress):
    return os.path.splitext(os.path.basename(wholeAddress))[1]



# a string as input.
# If it's a int, returns a int,
# if it's a float, returns a float,
# otherwise, returns a string
def castToWhatItShouldBe(val):

    # trying to cast to number
    try:
        # cast to float
        val = float(val)

        # if interger, cast to integer
        if(val.is_integer()):
            val = int(val)
        else:
            None

    except ValueError as e:
        None

    return val



# reads a text file and return a string of its content
def loadTextFile(fileAddress):
    strContent = ""

    try:
        with open(fileAddress) as f:
            content = f.readlines()

            strContent = "".join(content)
    except IOError as e:
        print("ERROR : file " + fileAddress + " not found.")

    return strContent


# return the timestamp in integer
def getTimestamp():
    return int(time.time())


# take a integer timestamp (can be a string as well) and return the date
# in a more readable format
def getDateFromTimestamp(ts):
    return datetime.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')
