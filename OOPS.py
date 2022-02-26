#class Paras:
   # def __init__(self, name, age):
    #    self.name = name
     # = Paras("Paras", 23)

#print(saxena.name + " is " + str(saxena) + " year(s) old.")
#print(saxena.name)
#print(saxena.age)


# Example 1: Creating a class and object with class and instance attributes

# class Dog:

    # class attribute
 #   attr1 = "mammal"

    # Instance attribute
  #  def __init__(self, name):
   #     self.name = name

# Roadger = Dog("Rodger")
# Tommy = Dog("Tommy")

# Accessing class attributes
# print("Roadger is a {}".format(Roadger.__class__.attr1))
# print("Tommy is a {}".format(Tommy.__class__.attr1))

# Accessing Instance attributes
# print("My name is {}".format(Roadger.name))
# print("My name is {}".format(Tommy.name))


# Example 2: Creating Class and objects with methods

class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name
		
	def speak(self):
		print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()

# Copy Constructor and Deep Copy

import copy

# Original list
li1 = [1, 2, [3, 5], 4]

# using deep copy to deep copy
li2 = copy.deepcopy(li1)

# original elements of list
print("The original elements before deep copying")

for i in range(0, len(li1)):
    print(li1[i], end=" ")
print("\r")

# adding and element to new list
li2[2][0] = 7

# change is reflected in li2
print ("The new list of elements after deep copying")
for i in range(0, len(li1)):
    print(li2[i], end="")
print("\r")

# Change is not reflected of deep copy
# As it as a deep copy

print ("The original elements after deep copying")
for i in range(0, len(li1)):
    print(li1[i], end="")

print("\r")


# Copy will create a new object in memory, and then assign the variable to that.

import copy

node = [0, 1]
node2 = node
node3 = copy.copy(node)

node2.append(5)

print(node)
print(node2)
print(node3)