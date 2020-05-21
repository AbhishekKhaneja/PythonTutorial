from PythonBasics.Functions import abc


class Inheriti(abc):
    num2 = 200

    def __init__(self):
        abc.__init__(self, 2, 4)

    def completedata(self):
     return self.num2 + self.num + self.summation()

object = Inheriti()
print(object.completedata())