import glob
import os

import numpy as np
import cv2
import matplotlib.pyplot as plt


def openImageFolder(folder):
    imageList = sorted(glob.glob(folder + os.sep + "*.[jJ][pP][gG]"))

    gaussianFilterSize = 5

    cvImgList = []


    for f in range(0, len(imageList) ):

        print("current : " + imageList[f])

        # loading images
        cvImgList.append(cv2.imread(imageList[f]))

        # start the process when a sufficiant number of image is loaded,
        # it must not be run until the end
        if(f >=  gaussianFilterSize):
            subArray = cvImgList[f-gaussianFilterSize : f]
            subArrayNames = imageList[f-gaussianFilterSize : f]
            filtered = gaussanFilterT(subArray)
            cv2.imwrite(imageList[f - gaussianFilterSize/2] + "_filtered_" + str(gaussianFilterSize) +  ".jpg" ,filtered)


# temporal gaussian filte
def gaussanFilterT(imgList):
    numberOfImages = len(imgList)
    mu = 0
    sigma = numberOfImages/7.

    # indexes
    x = np.arange(-(numberOfImages/2), (numberOfImages/2)+1)

    # weights
    y = 1./(sigma * np.sqrt(2. * np.pi)) * np.exp( - (x - mu)**2. / (2. * sigma**2.) )

    res = y[0] * imgList[0]

    for i in range(1, len(imgList)):
        res = res + y[i] * imgList[i]

    return res


if __name__ == '__main__':

    openImageFolder("/Users/jonathanlurie/Documents/code/pythonStuff/openCV_tests/images")

    exit()

    # must be odd because the "center" image must have more weight
    numberOfImages = 111

    # the data are 0-centered
    mu = 0

    # it appears that when standard dev is a seventh of N, we can sum up
    # the proportions up to more than 99%
    sigma = numberOfImages/7.



    x = np.arange(-(numberOfImages/2), (numberOfImages/2)+1)
    y = 1./(sigma * np.sqrt(2. * np.pi)) * np.exp( - (x - mu)**2. / (2. * sigma**2.) )


    print x
    print y
    print("sum : " + str(y.sum()))
    print("weight of central image : " + str(y[(numberOfImages/2)]))

    #print y

    plt.plot(x, y)


    plt.show()
