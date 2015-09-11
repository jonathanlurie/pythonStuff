from collections import Counter
import string
import os
import sys

# take a string, clean it and return an array of words
def cleanString(s):
    stripped = s.strip().lower()

    # remove puntuation
    #noPunk = stripped.translate(string.maketrans("",""), string.punctuation)

    replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
    noPunk = stripped.translate(replace_punctuation)


    # splitting into words with whitespaces
    listOfWord = noPunk.split(' ')

    # removing the empties
    noEmpties = filter(None, listOfWord)

    return noEmpties



def printHelp():
    print("\nERROR: This app needs an existing txt file as argument.\n")




if __name__ == "__main__":

    # the app need an argument
    if(len(sys.argv) != 2):
        printHelp()
        exit()


    # the file to open
    fileToOpen = str(sys.argv[1])


    # does the file in argument exist?
    if(not os.path.isfile(fileToOpen)):
        printHelp()
        exit()


    # constructing the counter
    cntr = Counter()

    # initialize the counter of ALL words
    globalCounter = 0

    # open a text file and read it line by line
    with open(fileToOpen) as fp:
        for line in fp:
            # clean the string
            cleanStringArray = cleanString(line)

            # count the global number of word
            globalCounter = globalCounter + len(cleanStringArray)

            # update the Counter
            cntr.update(cleanStringArray)



    # printing the first 1000,
    # except if there is less than 1000 in the counter
    thousand = 1000

    if(len(cntr) < thousand):
        thousand = len(cntr)


    # prepare to write the result in a file
    outFile = os.path.splitext(os.path.basename(fileToOpen))[0] + "_wordCount.txt"
    report = open(outFile,'w')



    # get the "thousand" most common words
    mostCommon = cntr.most_common(thousand)

    # just to display word rank in the repport
    wordIndex = 0

    # write the report with the "thousand" most common words
    for it in mostCommon:
        # compute the percent of presence of this word among the whole text
        percentOfUse = float(it[1]) / float(globalCounter)
        print percentOfUse
        report.write(str(wordIndex) + "\t" + it[0] + "\t" + str(percentOfUse) + "\n")

        wordIndex = wordIndex + 1


    print("\nINFO: the report was writen in the input folder as:")
    print(outFile)
    print("\n")

    report.close()
