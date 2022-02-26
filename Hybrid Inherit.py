class School:
    def func1(self):
        print("This function is in school")

class Student1:
    def func2(self):
        print("This function is in student1")

class Student2:
    def func3(self):
        print("This function is in student2")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student3")

object = Student3()
object.func1()
object.func2()

