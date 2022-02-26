# class Employee:

    # Initializing
  #  def __init__(self):
  #      print('Employee Created')

    # Calling destructor
   # def __del__(self):
       # print('Destructor called')

# def Create_obj():
  #  print('Making Object..')
   # obj = Employee()
   # print('function end')
   #  return obj

# print('Calling Create_obj() function...')    
# obj = Create_obj()
# print('Program End')


# Example-> 1
class A:
    def __init__(self, bb):
        self.b = bb
class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")

def fun():
    b = B()
fun()
