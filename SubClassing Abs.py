import abc

class parent:
    def paras(self):
        pass

class child(parent):
    def para(self):
        print("child class")

print(issubclass(child, parent)) 
print(issubclass(child, parent))       

