import numpy as np
import matplotlib.pyplot as plt


class operations():
	''' define a class of operations, rotation, translation, and Boolean, to be inherited by all shapes.'''
	def __init__(self):
		
		self.x = 0
		self.y = 0
		self.theta = 0	

	def translate(self, x_trans, y_trans):
		
		self.x += x_trans
		self.y += y_trans

	def rotation_angle(self, theta):
		
		self.theta = theta
	
	def apply_rotation(self, x, y):

		x_out = (x) * np.cos(self.theta) - (y) * np.sin(self.theta)
		y_out = (x) * np.sin(self.theta) + (y) * np.cos(self.theta)
		return x_out, y_out

	def union(*shapes):

		return lambda x, y: np.min([shape.eqn(x, y) for shape in shapes], 0)

	def intersection(*shapes):
		
		return lambda x, y: np.max([shape.eqn(x, y) for shape in shapes], 0)
	



class Circle(operations): # a circle class, defined by radius and centre point

	def __init__(self, x_cent = 0, y_cent = 0, radius = 1):

		operations.__init__(self)
		self.radius = radius
		self.x += x_cent
		self.y += y_cent

	def eqn(self, x, y):
		
		return (self.x - x)**2 + (self.y - y)**2 - self.radius**2


class Square(operations): # a square class, defined by centre and side length

	def __init__(self, x_cent = 0, y_cent = 0, side = 1):

		operations.__init__(self)
		self.x += x_cent
		self.y += y_cent
		self.side = side

	def eqn(self, x, y):

		x, y = self.apply_rotation(x, y) # rotations are applied when the equation is called.

		return abs((self.x - x) / self.side + (self.y -y) / self.side) + abs((self.x - x) / self.side - (self.y - y) / self.side) - 2



def display_2d(function):

	x_min, x_max = (-3,3)
	y_min, y_max = (-3,3)

	fig = plt.figure()
	ax = fig.add_subplot(111, aspect='equal')

	x, y = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(x_min, x_max, 100))

	z = function(x,y)	
	contour_map = ax.contour(x, y, z, [0], colors='k')
	plt.axis('off')    

	plt.show()

circle1 = Circle() # instantiate shapes
square1 = Square()
circle2 = Circle()

circle1.translate(-1/2., 0) # translate
square1.translate(1/2., 1/2.)
circle2.translate(1, 0)

square1.rotation_angle(np.pi/4.) # define a rotation angle for the square

composite_u = circle1.union(square1, circle2)
composite_i = circle1.intersection(square1, circle2)


display_2d(composite_u) # plot

