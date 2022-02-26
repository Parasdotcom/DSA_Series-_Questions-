class Parent:
    def func1(self):
        print("This function is in parent class")

class Child(Parent):
    def func2(self):
        print("This function is in child class")

object = Child()
object.func1()
object.func2()


class Child:

    # constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is student
    def isStudent(self):
        return False

class Student(Child):

    # True is returned
    def isStudent(self):
        return True

# An Object of child
std = Child("Raja")
print(std.getName(), std.isStudent())

# An object of student
std = Student("Paras")
print(std.getName(), std.isStudent())