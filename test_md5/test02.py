#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''
import fnmatch
import os


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


def main():
    filesFound = listFiles("/Users/jonathanlurie/Documents/photos", "*.jpg", False)

    for f in filesFound:
        print f


if __name__ == '__main__':
    main()
