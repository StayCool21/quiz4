from typing import Protocol

class Shape(Protocol):
    def area(self) -> None:
        pass

    def perimeter(self) -> None:
        pass

class Square:
    def __init__(self, side_length:int) -> None:
        self.side_length = side_length

    def area(self) -> int:
        return self.side_length ** 2
    
    def perimeter(self) -> int:
        return 4 * self.side_length
    
class Rectangle:
    def __init__(self, width:int, length:int) -> None:
        self.width = width
        self.length = length
    
    def area(self) -> int:
        return self.width * self.length
    
    def perimeter(self) -> int:
        return (2 * self.width) + (2 * self.length)
    
squareObj = Square(3)
rectangleObj = Rectangle(2, 5)

print('Square Area:', squareObj.area())
print('Square Perimeter:', squareObj.perimeter())

print('Rectangle Area:', rectangleObj.area())
print('Rectangle Perimeter:', rectangleObj.perimeter())