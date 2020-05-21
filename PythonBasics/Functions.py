class abc:
    num = 100
    def __init__(self, a, b):
        self.first = a
        self.second = b
        print("i am a default constructor and called automatically when a object is created")

    def indian(self):
        print("i am a indian nothing to do with hindu muslim")

    def summation(self):
        return self.first + self.second + abc.num


obj = abc(10, 20)  # Syntax to create object in python no new keyword i s required like in java
obj.summation()
abc.indian(obj)
print(obj.num)

#def abhi(name):
#    print("name is " + name)

#def addition (a, b):
    #return a+b


#abhi("Abhishek")

#System =addition(10,20)
#print(System)
