### 1 ###

countries = ["Malaysia", "Singapore", "Thailand", "Brunei", "Indonesia", 
"Japan", "China", "India", "South Korea", "Vietnam" ]

def search(name):
	if name in countries:
		print(name)
	else:
		print("Not Found")


### 2 ###
import math

class Animal:

	x_coordinates = 0
	y_coordinates = 0

	def __init__(self):
		raise TypeError("Not instantiable")

	# def __init__(self, x, y):
	# 	self.x_coordinates = x
	# 	self.y_coordinates = y

	def moveUp(self):
		self.y_coordinates += 1

	def moveDown(self):
		self.y_coordinates -= 1

	def moveLeft(self):
		self.x_coordinates -= 1

	def moveRight(self):
		self.x_coordinates += 1


class Dog(Animal):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self, cat):
		return math.sqrt((self.x-cat.x) ** 2 + (self.y-cat.y) ** 2)


class Cat(Animal):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self, dog):
		return math.sqrt((self.x-dog.x) ** 2 + (self.y-dog.y) ** 2)



### TEST ###

# instantiable or not?
#x = Animal() 

# check distance output
snoopy = Dog(-7,-4)
garfield = Cat(17, 6.5)
D = snoopy.distance(garfield)
print(D) # maybe need to set to 6 decimal places?
 
