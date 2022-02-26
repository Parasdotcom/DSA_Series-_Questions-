# num = 5
# print(n)

# Getting the memory address of an object 
# returns a unique integer representing 
# the position of the object in memory.

#an_object = {"a": 5}
#object_id = id(an_object)
#print(object_id)

# Python is a imutable function id() 
# returns the object's memory address.
#x = 5
#id(x)
# is return True if and only 
# if two objects have the same memory address.
#x += 1
#x
#id(x)
# Even though the above code appears to modify 
# the value of x, you’re getting 
# a new object as a response.


# str is a immutable
# s = "paras_saxena"
# id(s)
# s += "raja"
# s
# id(s)

#x = 5
#y = x
#5

#x = 4
#y = 7
#print((x), (y))

# Function to pointers
# A function is a block of code 
# which only runs when it is called.

# You can pass data, 
# known as parameters, into a function.
# A function can return data as a result.

# def my_function(food):
    #for x in food:
       # print(x)
#fruits = ["orange", "banana", "mango"]
#id(fruits)
#my_function(fruits)

# return the function
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))