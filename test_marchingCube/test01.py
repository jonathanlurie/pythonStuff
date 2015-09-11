#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Generate spheres two different ways with pyMCubes,
              using marching cube algorithm and Collada format.
link        : https://github.com/pmneila/PyMCubes
              http://pycollada.readthedocs.org/en/v0.4/

'''
import numpy as np
import mcubes


def sphere1():
    # Create a data volume (30 x 30 x 30)
    X, Y, Z = np.mgrid[:50, :50, :50]
    u = (X-25)**2 + (Y-25)**2 + (Z-25)**2 - 20**2

    # Extract the 0-isosurface
    vertices, triangles = mcubes.marching_cubes(u, 0)

    print vertices.shape

    print triangles.shape
    #for t in vertices:
    #    print t



    # Export the result to sphere.dae
    mcubes.export_mesh(vertices, triangles, "sphere3.dae", "MySphere")

def plan():
    # Create a data volume (30 x 30 x 30)
    X, Y, Z = np.mgrid[:50, :50, :50]
    u = (3*X) + (2*Y) + (1*Z)

    # Extract the 0-isosurface
    vertices, triangles = mcubes.marching_cubes(u, 0)

    print vertices.shape

    print triangles.shape
    #for t in vertices:
    #    print t



    # Export the result to sphere.dae
    mcubes.export_mesh(vertices, triangles, "plan.dae", "MyPlane")



def torus():

    size = 100
    X, Y, Z = np.mgrid[:size, :size, :size]

    r = size / 8
    R = r * 2
    u = ( (X-size/2)**2 + (Y-size/2)**2 + (Z-size/2)**2 + R**2 -r**2)**2 - 4*(R**2)*((X-size/2)**2 + (Y-size/2)**2)


    # Extract the 0-isosurface
    vertices, triangles = mcubes.marching_cubes(u, 0)

    # Export the result to sphere.dae
    mcubes.export_mesh(vertices, triangles, "torus1.dae", "MyTorus")

def sphere2():
    # Create the volume
    f = lambda x, y, z: x**2 + y**2 + z**2

    # Extract the 16-isosurface
    vertices, triangles = mcubes.marching_cubes_func((-10,-10,-10), (10,10,10),100, 100, 100, f, 16)

    # Export the result to sphere2.dae
    mcubes.export_mesh(vertices, triangles, "sphere2.dae", "MySphere")


if __name__ == '__main__':
    sphere1()
