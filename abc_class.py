from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return 4 * self.side_length
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (2 * self.width) + (2 * self.length)
    
squareObj = Square(3)
rectangleObj = Rectangle(2, 5)

print('Square Area:', squareObj.area())
print('Square Perimeter:', squareObj.perimeter())

print('Rectangle Area:', rectangleObj.area())
print('Rectangle Perimeter:', rectangleObj.perimeter())