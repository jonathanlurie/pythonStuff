#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''
import sys
import cv2
import numpy as np
import collada
import mcubes


def main():
    if(len(sys.argv) != 3):
        print("Missing argument:")
        print("1- input DEM tile")
        print("2- output DAE file")
        exit()

    inputDEM = sys.argv[1]



    # -1 arg means read image as is, instead of forcing 8bit RGB
    img = cv2.imread(inputDEM, -1)
    #img = cv2.imread("srtm_54_07/srtm_54_07_CROP.tif", -1)


    # just printing a value
    #print img[100, 250]

    # finding extremas
    arrayMin = np.amin(img)
    arrayMax = np.amax(img)



    # make the DEM "stick to ground", and keep propostion
    # (SRTM precision : 90m/pixel)
    #imgGround = np.subtract(img, arrayMin) / 90.
    imgGround = np.subtract(img, 0.) / 90.

    make3DEM(imgGround)

def make3DEM(img):

    outputDAE = sys.argv[2]

    #print img
    #print img
    xSize = img.shape[1]
    ySize = img.shape[0]

    zSize = np.amax(img)

    vertices = np.array([])
    triangles = np.array([])
    normales = np.array([])

    progressStatus = None

    # loops for vertices
    for iy in range(0, ySize-1):

        print "vertices : " + str(round(float(iy)/float(ySize)*100., 2)) + "%"

        tmpVertices = np.array([])
        for ix in range(0, xSize-1):

            # first row
            if(ix == 0 and iy == 0):
                a = np.array([ ix, iy, img[ix, iy] ])
                b = np.array([ ix+1, iy, img[ix+1, iy] ])
                c = np.array([ ix+1, iy+1, img[ix+1, iy+1] ])
                d = np.array([ ix, iy+1, img[ix, iy+1] ])
                tmpVertices = np.append(tmpVertices, [a, b, c, d])

            elif(iy == 0):
                b = np.array([ ix+1, iy, img[ix+1, iy] ])
                c = np.array([ ix+1, iy+1, img[ix+1, iy+1] ])
                tmpVertices = np.append(tmpVertices, [b, c])

            elif(ix == 0):
                c = np.array([ ix+1, iy+1, img[ix+1, iy+1] ])
                d = np.array([ ix, iy+1, img[ix, iy+1] ])
                tmpVertices = np.append(tmpVertices, [c, d])

            else:
                c = np.array([ ix+1, iy+1, img[ix+1, iy+1] ])
                tmpVertices = np.append(tmpVertices, [c])

        vertices = np.append(vertices, tmpVertices)

        # flushing console progress
        sys.stdout.write("\033[F")

    vertices.shape = (-1, 3)

    print len(vertices)
    #print vertices
    #print vertices[1]
    #print vertices[1][2]
    '''
    ct = 0
    for v in vertices:
        print ct
        print v
        ct = ct + 1
        print ""

    exit()
    '''


    #firtRowSum = ((xSize - 1) * 2 ) + 3
    firtRowSum = (xSize * 2) - 1

    # loops for triangles
    for iy in range(0, ySize-1):
        #print str(iy)
        print "triangles : " + str(round(float(iy)/float(ySize)*100., 2)) + "%"

        tmpTriangles = np.array([])

        for ix in range(0, xSize-1):



            # (0, 0)
            if(ix == 0 and iy == 0):
                aIndex = 0
                bIndex = 1
                cIndex = 2
                dIndex = 3

            # (1, 0)
            elif(ix == 1 and iy == 0):
                aIndex = ix
                bIndex = (ix * 2) + 2
                cIndex = (ix * 2) + 3
                dIndex = ((ix-1) * 2) + 2

            # (0, 1)
            elif(ix == 0 and iy == 1):
                aIndex = 3
                bIndex = 2
                cIndex = firtRowSum + 1
                dIndex = firtRowSum + 2

            # (1, 1)
            elif(ix == 1 and iy == 1):
                aIndex = 2
                bIndex = 5
                cIndex = firtRowSum + 3
                dIndex = firtRowSum + 1

            # 1st row (except 1st col)
            elif(iy == 0):
                aIndex = ix * 2
                bIndex = (ix * 2) + 2
                cIndex = (ix * 2) + 3
                dIndex = ((ix-1) * 2) + 3

            # 2nd row (except 1st and 2nd col)
            elif(iy == 1):
                aIndex = (ix * 2) + 1
                bIndex = (ix * 2) + 3
                cIndex = firtRowSum + 2 + ix
                dIndex = firtRowSum + 1 + ix

            # 1st col (except 1st and 2nd row)
            elif(ix == 0):
                aIndex = firtRowSum + (iy - 2) * xSize + 2
                bIndex = firtRowSum + (iy - 2) * xSize + 1
                cIndex = firtRowSum + (iy - 1) * xSize + 1
                dIndex = firtRowSum + (iy - 1) * xSize + 2

            # 2nd col (except 1st and 2nd row)
            elif(ix == 1):
                aIndex = firtRowSum + (iy - 2) * xSize + 1
                bIndex = firtRowSum + (iy - 2) * xSize + 3
                cIndex = firtRowSum + (iy - 1) * xSize + 3
                dIndex = firtRowSum + (iy - 1) * xSize + 1

            # all other cases
            else:
                aIndex = firtRowSum + xSize * (iy - 2) + ix + 1
                bIndex = firtRowSum + xSize * (iy - 2) + ix + 2
                cIndex = firtRowSum + xSize * (iy - 1) + ix + 2
                dIndex = firtRowSum + xSize * (iy - 1) + ix + 1


            # Add triangle T1, vertices a, b, c
            t1 = np.array([ aIndex, bIndex, cIndex ])
            tmpTriangles = np.append(tmpTriangles, t1)

            # Add triangle T2, vertices a, c, d
            t2 = np.array([ aIndex, cIndex, dIndex ])
            tmpTriangles = np.append(tmpTriangles, t2)


            '''
            print "( " + str(ix) + " , " + str(iy) + " )"
            print aIndex
            print bIndex
            print cIndex
            print dIndex
            '''


            '''
            # computation of vectors
            vAB = vertices[bIndex] - vertices[aIndex]
            vAC = vertices[cIndex] - vertices[aIndex]
            vAD = vertices[dIndex] - vertices[aIndex]

            # computation of norm vectors
            t1Norm = computeNormVector(vAB, vAC)
            t2Norm = computeNormVector(vAC, vAD)

            normales = np.append(normales, t1Norm)
            normales = np.append(normales, t2Norm)
            '''


        triangles = np.append(triangles, tmpTriangles)

        # flushing console progress
        sys.stdout.write("\033[F")

    triangles.shape = (-1, 3)
    #normales.shape = (-1, 3)

    '''
    ct = 0
    for t in triangles:
        print ct
        print t
        ct = ct + 1
        print ""
    '''

    print("Exporting...")


    export_mesh(vertices, triangles.astype(int), outputDAE)

# vA and vB are 3D vectors, in shape of a numpy array
def computeNormVector(vA, vB):
    x = (vA[1] * vB[2]) - (vA[2] * vB[1])
    y = (vA[2] * vB[0]) - (vA[0] * vB[2])
    z = (vA[0] * vB[2]) - (vA[2] * vB[0])

    norm = ((x**2) + (y**2) + (z**2))**0.5

    return np.array([ x/norm, y/norm, z/norm])



def export_mesh(vertices, triangles, filename, mesh_name="mcubes_mesh"):
    """
    Exports a mesh in the COLLADA (.dae) format.

    Needs PyCollada (https://github.com/pycollada/pycollada).
    """



    mesh = collada.Collada()

    vert_src = collada.source.FloatSource("verts-array", vertices, ('X','Y','Z'))
    geom = collada.geometry.Geometry(mesh, "geometry0", mesh_name, [vert_src])

    input_list = collada.source.InputList()
    input_list.addInput(0, 'VERTEX', "#verts-array")



    triset = geom.createTriangleSet(triangles, input_list, "")
    geom.primitives.append(triset)
    mesh.geometries.append(geom)

    geomnode = collada.scene.GeometryNode(geom, [])
    node = collada.scene.Node(mesh_name, children=[geomnode])

    myscene = collada.scene.Scene("mcubes_scene", [node])
    mesh.scenes.append(myscene)
    mesh.scene = myscene

    mesh.write(filename)

'''
def createCollada():
    from collada import *

    mesh = Collada()
    effect = material.Effect("effect0", [], "phong", diffuse=(1,0,0), specular=(0,1,0))
    mat = material.Material("material0", "mymaterial", effect)
    mesh.effects.append(effect)
    mesh.materials.append(mat)

    vert_floats = [-50,50,50,
                    50,50,50,
                    -50,-50,50,
                    50, -50,50,
                    -50,50,-50,
                    50,50,-50,
                    -50,-50,-50,
                    50,-50,-50]

    normal_floats =    [0,0,1,  0,0,1,  0,0,1,  0,0,1,
                        0,1,0,  0,1,0,  0,1,0,  0,1,0,
                        0,-1,0, 0,-1,0, 0,-1,0, 0,-1,0,
                        -1,0,0, -1,0,0, -1,0,0, -1,0,0,
                        1,0,0,  1,0,0,  1,0,0,  1,0,0,
                        0,0,-1, 0,0,-1, 0,0,-1, 0,0,-1]
    print len(normal_floats)
    vert_src = source.FloatSource("cubeverts-array", np.array(vert_floats), ('X', 'Y', 'Z'))

    normal_src = source.FloatSource("cubenormals-array", np.array(normal_floats), ('X', 'Y', 'Z'))

    geom = geometry.Geometry(mesh, "geometry0", "mycube", [vert_src, normal_src])

    input_list = source.InputList()
    input_list.addInput(0, 'VERTEX', "#cubeverts-array")
    input_list.addInput(1, 'NORMAL', "#cubenormals-array")

    indices = np.array([0,0,2,1,3,2,0,0,3,2,1,3,0,4,1,5,5,6,0, 4,5,6,4,7,6,8,7,9,3,10,6,8,3,10,2,11,0,12,4,13,6,14,0,12,6,14,2,15,3,16,7,17,5,18,3,16,5,18,1,19,5,20,7,21,6,22,5,20,6,22,4,23])

    print len(indices)

    triset = geom.createTriangleSet(indices, input_list, "materialref")
    geom.primitives.append(triset)
    mesh.geometries.append(geom)

    matnode = scene.MaterialNode("materialref", mat, inputs=[])
    geomnode = scene.GeometryNode(geom, [matnode])
    node = scene.Node("node0", children=[geomnode])

    myscene = scene.Scene("myscene", [node])
    mesh.scenes.append(myscene)
    mesh.scene = myscene

    mesh.write('cube.dae')

'''

def crop():
    # -1 arg means read image as is, instead of forcing 8bit RGB
    img = cv2.imread("DEM/srtm_38_03.tif", -1)
    crop_img = img[2200:2500, 2200:2500] # Crop from x, y, w, h -> 100, 200, 300, 400

    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)

    # save it
    cv2.imwrite('DEM/srtm_38_03_CROP.tif',crop_img)




if __name__ == '__main__':

    #createCollada()


    #make3DEM(None)

    main()
