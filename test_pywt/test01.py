#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Wavelet decomposition / recomp as seen on
            : http://stackoverflow.com/questions/24536552/how-to-combine-pywavelet-and-opencv-for-image-processing

'''

import numpy as np
import pywt
import cv2

def w2d(img, mode='haar', level=1):
    imArray = cv2.imread(img)
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    #convert to float
    imArray =  np.float32(imArray)
    imArray /= 255.;
    # compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #print len(coeffs)

    #Process Coefficients
    coeffs_H=list(coeffs[1][0])
    coeffs_H *= 0
    coeffs[1][0] = coeffs_H

    # reconstruction
    imArray_H=pywt.waverec2(coeffs, mode);
    imArray_H *= 255.;
    imArray_H =  np.uint8(imArray_H)
    #Display result
    cv2.imshow('image',imArray_H)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == '__main__':
    #print pywt.families()
    #print pywt.wavelist('db')
    w2d("image_512.jpg",'db6',1)
