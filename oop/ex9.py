from abc import ABC, abstractmethod

# abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# child class
class Square(Shape):
    def area(self):
        print("Area of square")

s = Square()
s.area()