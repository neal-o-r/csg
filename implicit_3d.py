from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def sphere(x,y,z):
    # Implicit function of a sphere a (0,0) with radius 2 
    return x**2 + y**2 + z**2 - 2**2


def nordstrand(x,y,z):
    # Implicit function of Nostrand's Weird Surface
    return 25 * ((x**3) * (y+z) + (y**3) * (x+z) + (z**3) * (y+x)) + 50 * (x**2 * y**2 + x**2 * z**2+ y**2 * z**2) - 125*(x**2 * y*z + y**2 *x*z + z**2 * x*y) + 60*x*y*z - 4*(x*y +x*z + y*z)


def implicit_3d(function):
    ''' A script which accepts an implicit function as an input and renders it using a simple contour map'''
   
    x_min, x_max = -2., 2
    y_min, y_max = -2., 2
    z_min, z_max = -2., 2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    grid_1,grid_2 = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(x_min, x_max, 100)) # 2d plane mesh


    for plane in np.linspace(x_min, x_max, 15): # plot contours in 15 planes on each axis
        
        x = function(plane, grid_1, grid_2) # get the values of the function on the grid points in this plane
        contour_x = ax.contour(x+plane, grid_1, grid_2, [plane], zdir='x') 
        # plot a contour map of the values in that plane.
        # the [plane] specifies that these contours have the value 'plane', that is, all points plotted will be of the form (plane, plane). We could only plot the zeros by replacing this with [0], which might be *more* implicit, but the visulisation is less clear with only points of the form (0,plane)

        y = function(grid_1, plane, grid_2) # repeat for y & z
        contour_y = ax.contour(grid_1, y+plane, grid_2, [plane], zdir='y')
        
        z = function(grid_1, grid_2, plane)
        contour_z = ax.contour(grid_1, grid_2, z+plane, [plane], zdir='z')

  

    ax.set_zlim3d(z_min,z_max) # add limits
    ax.set_xlim3d(x_min,x_max)
    ax.set_ylim3d(y_min,y_max)

    plt.show()

''' This code could be expanded by using python's lambda calculus to implement a union or intersection operation, allowing functions to be combined as in CSG.''' 

#implicit_3d(nordstrand)
implicit_3d(sphere)
