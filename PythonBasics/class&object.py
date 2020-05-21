class india:
    num =100 # this is a class variable

    # default constructor - Note whethjer we create a default constructor or not it is being called at runtime by the compiler
    def __init__(self,a , b):

        self.first = a
        self.second = b
        print("i am a default constructor and called automatically when a object is created")
    def indian(self):
        print("i am a indian nothing to do with hindu muslim")

    def summation(self):
        print(self.first + self.second + india.num)

obj = india(10,20) # Syntax to create object in python no new keyword i s required like in java
obj.summation()
india.indian(obj)
print(obj.num)


#obj1 = india(20,30) # Syntax to create object in python no new keyword i s required like in java
#obj1.summation()
#print(obj1.num)