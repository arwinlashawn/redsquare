### 1 ###

countries = ["Malaysia", "Singapore", "Thailand", "Brunei", "Indonesia", 
"Japan", "China", "India", "South Korea", "Vietnam" ]

def search(name):
	if name.title() in countries:
		print(name.title())
	else:
		print("Not Found")

# uppercase
search("vietnaM")

### 2 ###
from abc import ABC, abstractmethod
import math

class Animal(ABC):

	x_coordinates = 0
	y_coordinates = 0

# not optimal to make it abstract
# abc meta
# using abstactmethod to make Animal uninstantiable
	@abstractmethod
	def __init__(self, x, y):
		self.x = x
		self.y = y

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
		super().__init__(x, y)

	def distance(self, cat):
		return math.sqrt((self.x-cat.x) ** 2 + (self.y-cat.y) ** 2)


class Cat(Animal):

	def __init__(self, x, y):
		super().__init__(x, y)

	def distance(self, dog):
		return math.sqrt((self.x-dog.x) ** 2 + (self.y-dog.y) ** 2)



### TEST ###

# instantiable or not?
#x = Animal() 

# check distance output
snoopy = Dog(0,3)
garfield = Cat(4, 0)
pussinboots = Cat(3,0)
D = snoopy.distance(garfield)

print(D) # maybe need to set to 6 decimal places?

