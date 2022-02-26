class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely used is spoken in India.")

    def type(self):
        print("India is developing country.")            

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English os the most widely used is spoken in USA.") 

    def type(self):
        print("USA is developed country.")

obj_ind = India()
obj_usa = USA()
for country in(obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
