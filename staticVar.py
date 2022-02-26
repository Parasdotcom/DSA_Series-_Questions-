# Static Variable

class Car:
    # define the class variable or static variable or class car
    num = 7
    msg = "This is a good Car"

obj = Car()

# Access a static variable num using the class name with a dot 
# pointer.
print("Lucky No.", Car.num)
print(Car.msg)



# Static Function

class Marks:
    def Math_num(a,b):
        return a + b

    def Sci_num(a,b):
        return a + b    

    def Eng_num(a,b):
        return a + b

print("Total Marks in Math", Marks.Math_num(70,15))

print("Total Marks in Science", Marks.Sci_num(64,28))

print("Total Marks in English", Marks.Eng_num(70,20))