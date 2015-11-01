#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : TheGrowingBox is a set of simple methods I use for my projects.
              It deals with filepath, checksum, and file listing.

'''

import os
import time
import datetime
import fnmatch
import hashlib
import urllib2
import re



def getBasenameNoExt(wholeAddress):
    """Get the basename of a filepath without extension

    Parameters:
        wholeAddress - filepath string to a file
    """
    return os.path.splitext(os.path.basename(wholeAddress))[0]


def getBasenameWithExt(wholeAddress):
    """Get the basename of a filepath

    Parameters:
        wholeAddress - filepath string to a file
    """
    return os.path.basename(wholeAddress)


def getFolderName(wholeAddress):
    """Return the parent folder of a filepath.

    Parameters:
        wholeAddress - filepath string to a file
    """
    return os.path.dirname(wholeAddress)


def getFileExt(wholeAddress):
    """return the extension of a file.

    Parameters:
        wholeAddress - string of a filepath
    """
    return os.path.splitext(os.path.basename(wholeAddress))[1]


def castToWhatItShouldBe(val):
    """Cast a string into the proper numeral type if possible.

    If the string is actually a float, a float will be returned.
    If the string is actually a integer , an integer will be returned.
    If the string is none of them, it will return the string itself.

    Parameters:
        val - string to convert
    """

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


def loadTextFile(fileAddress):
    """Loads a text file into a string

    Parameters:
        fileAddress - path to a text file
    """

    strContent = ""

    try:
        with open(fileAddress) as f:
            content = f.readlines()

            strContent = "".join(content)
    except IOError as e:
        print("ERROR : file " + fileAddress + " not found.")

    return strContent


def getTimestamp():
    """return the timestamp in integer
    """

    return int(time.time())


def getDateFromTimestamp(ts):
    """Transforms a timestamp into a date string.

    The format of the date is YYYY-MM-DD HH:mm:ss

    Parameters:
        ts - timestamp as integer or string.
    """

    return datetime.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')


def md5(fname):
    """Compute md5 checksum of a file.

    Compatible with big files.

    Parameters:
        fname - path of a file
    """

    hash = hashlib.md5()
    with open(fname) as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash.update(chunk)
    return hash.hexdigest()



def listFiles(rootFolder, filePattern, relativeFromRootFolder=False):
    """Makes a list of files.

    No matter how many subfolders.

    Parameters:
        rootFolder - folder to search in, with all subfolders.
        filePattern - regex pattern, like "*.py"
        relativeFromRootFolder - True : write the rootFolder, False : stay relative (default : False)
    """

    matches = []
    for root, dirnames, filenames in os.walk(rootFolder):
        for filename in fnmatch.filter(filenames, filePattern):

            if(relativeFromRootFolder):
                matches.append(os.path.join(root, filename)[len(rootFolder):])
            else:
                matches.append(os.path.join(root, filename))


    return matches



# downloads a distant file to a local address
# using urllib2
# return True in case of success, False in other cases
def downloadFile(distantURL, localURL=None):

    distantFileName = getBasenameWithExt(distantURL)

    if(not localURL):
        localURL = distantFileName

    status = False

    try:

        # copy the file to local
        print("Downloading " + distantFileName + " ... ")
        distantFile = urllib2.urlopen(distantURL)
        localFile = open(localURL, 'wb')
        localFile.write(distantFile.read())
        localFile.close()
        print("\tDONE")
        status = False

    except urllib2.HTTPError as e:

        print("FAIL! (" + str(e.code) + ")")

    except urllib2.URLError as e:
        print("FAIL!")
        print("\nError status : " + str(e) )
        print("\nNote: Mapbox Studio need to be opened for tile downloading, is it?\n")

        exit()

    return status


# Natural sorting of files not using leading zeros.
# list as input, list as output
# Based on the answer of Mark Byers on StackOverflow.
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

# main tester
if __name__ == '__main__':
    # from and to are the same
    #copyFile("/Users/jonathanlurie/Documents/code/data/NEFpictures/_NIK4337.xmp", "/Users/jonathanlurie/Documents/code/data/NEFpictures/_NIK4337.xmp")
    # more regular
    #copyFile("/Users/jonathanlurie/Documents/code/data/NEFpictures/origCurve/_NIK4337.xmp", "/Users/jonathanlurie/Documents/code/data/NEFpictures/_NIK4337.xmp")
    #copyFile("/Users/jonathanlurie/Documents/code/data/NEFpictures/origCurve/_NIK4337.xmp", "/Users/jonathanlurie/Documents/code/data/NEFpictures/_NIK4337-2.xmp")
    #copyFile("/Users/jonathanlurie/Documents/code/data/NEFpictures/origCurve/_NIK4337.xmp", "/Users/jonathanlurie/Documents/code/data/NEFpictures/_NIK4337-3.xmp")

    #loadTextFile("/Users/jonathanlurie/Desktop/help.txt")

    downloadFile("https://github.com/jonathanlurie/BLANK_GOOEY/archive/master.zip", "/Users/jonathanlurie/Desktop/t3/f.zip")
