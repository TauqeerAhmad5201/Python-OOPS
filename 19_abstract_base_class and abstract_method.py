from abc import ABC, abstractclassmethod, abstractmethod

#abstract class -> it is a parent class which simply dictate the child classes to have to same some particular functions
class Shape():
    @abstractmethod
    def printarea(self):  #here it represents that child class should have printarea functions for sure.
        return 0

class Rectangle(Shape):
    type = "Rectange"
    sides = 4 
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def printarea(self):
        return self.length*self.breadth

r1 = Rectangle(float(input('Enter two numbers ')),float(input()))
print(r1.printarea())
