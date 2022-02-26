class Paras1:
    def m(self):
        print("In Paras1")

class Paras2:
    def m(self):
        print("In Paras2")

class Paras3:
    def m(self):
        print("In Paras3")

class Paras4:
    def m(self):
        print("In Paras4")

class Paras1(Paras2, Paras3):
    pass
obj = Paras4()
obj.m()    