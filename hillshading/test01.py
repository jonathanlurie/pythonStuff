#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''

import sys
import numpy as np
import math

import cv2


def main():
    inputDTM = "data/input/srtm_54_07_CROP_360.tif"

    sunPosition = np.array([-1000, -1000, 1000])
    sunIlluminationVector = sunPosition * -1.

    # casting the array to float on-the-fly to make it "derivable"
    img = cv2.imread(inputDTM, -1).astype(float)

    #print img.shape

    '''
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)
    maxi = np.max(sobelx)
    mini = np.min(sobelx)
    print maxi
    print mini



    print ""

    print sobelx
    '''

    diffx = np.diff(img, axis=1)
    diffy = np.diff(img, axis=0)
    #print img
    #print ""


    #print diffy

    normalImage = np.zeros((diffy.shape[0],diffx.shape[1],3), float)

    for iy in range(0, len(normalImage[0])):
        for ix in range(0, len(normalImage[1])):
            #
            normVect = computeNormVectorFromElevation(diffx[ix][iy], diffy[ix][iy])
            luminance = computeLuminanceFromVectorsIncidance(normVect, sunIlluminationVector)

            #print luminance


            if(ix==41 and iy==98):
                print img[ix][iy]

            normalImage[ix][iy][0] = luminance
            normalImage[ix][iy][1] = luminance
            normalImage[ix][iy][2] = luminance


    maxi = np.max(normalImage)


    normalImage = ( normalImage / maxi ) * 255

    cv2.imwrite("there.jpg", normalImage )


    #cv2.imwrite('data/output/sobelx.tif',sobelx)
    #cv2.imwrite('data/output/sobely.tif',sobely)


# using dX = 1, dY=1 and dZ=elevation,
def computeNormVectorFromElevation(dXele, dYele):
    vX = computeNormalizedVectorFromVector(np.array([1., 0., dXele]))
    vY = computeNormalizedVectorFromVector(np.array([0., 1., dYele]))
    n = computeVectorProduct(vX, vY, normalize=True)

    return n



# return the norm (aka. length) of a 3D vector.
# v must be a numpy array of size 3
def computeVectorNorm(v):
    return  ((v[0]**2) + (v[1]**2) + (v[2]**2))**0.5

# return a normalized vector, meaning a vector which norm is 1.
# input and output are both numpy array of size 3.
def computeNormalizedVectorFromVector(v):
    norm = computeVectorNorm(v)

    return np.array([v[0]/norm, v[1]/norm, v[2]/norm])


# compute the vector product (aka. cross product) of two vectors.
# If v1 and v2 are defining a plan, the vector product is the normal vector
# of this plan.
# both input and output are 3D vector : numpy array of size 3.
# if normalize is True, then the returned vector is normalized
def computeVectorProduct(v1, v2, normalize=False):
    nx = (v1[1] * v2[2]) - (v1[2] * v2[1])
    ny = (v1[2] * v2[0]) - (v1[0] * v2[2])
    nz = (v1[0] * v2[1]) - (v1[1] * v2[0])

    if(normalize):
        return computeNormalizedVectorFromVector(np.array([nx, ny, nz]))
    else:
        return np.array([nx, ny, nz])


# return the angle between 2 vectors.
# the angle is in radian, unless arg degree=True
# vectors must be numpy array of length 3
def computeVectorAngle(v1, v2, degree=False):
    sinTheta = computeVectorAngleSinus(v1, v2)

    # in radian (default)
    theta = math.asin(sinTheta)

    if(degree):
        theta = math.degrees(theta)

    return theta

# compute the sinus between two 3D vectors.
# both are numpy array of length 3
def computeVectorAngleSinus(v1, v2):
    normalVector = computeVectorProduct(v1, v2)
    normalVectorNorm = computeVectorNorm(normalVector)
    sinTheta = normalVectorNorm / (computeVectorNorm(v1) * computeVectorNorm(v2))

    # to prevent poor rounding
    if(sinTheta > 1):
        sinTheta = 1.
    if(sinTheta < -1):
        sinTheta = -1.

    return sinTheta

# v1 is a lightsource normal vector, v2 is the surface normal vector.
# If they are "looking" at each other, the luminance is max.
# the return value is normalized in a [0, 255] default interval
def computeLuminanceFromVectorsIncidance(v1, v2, minLumi=0., maxLumi=255.):

    # we first get the sinus between those two normal vectors
    angle = computeVectorAngle(v1, v2)

    # luminance rules:
    # - the luminance is max at 180/-180 degrees
    # - the luminance is half at 135/225 degrees
    # - the luminance is poor (almost none) at 90/-90
    # - the luminance is 0
    # this can be formulated like that:
    # lumi = (-cos( (0.56*theta)^2 ) * 0.5) + 0.5

    # lumi is defined between 0 and 1
    lumi = ( math.cos( (0.56 * angle)**2 ) * (-0.5) ) + 0.5

    #print math.degrees(angle)

    #lumi = lumi * maxLumi

    return lumi


if __name__ == '__main__':
    main()
