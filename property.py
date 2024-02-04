class Circle:
    def __init__(self, radius):
        self.set_radius(radius)

    def get_radius(self):
        return self._radius
    
    def set_radius(self, input):
        if (input <= 0):
            raise ValueError("Radius must be greater than zero.")
        self._radius = input

    def get_diameter(self):
        return 2 * self._radius
    
    def get_area(self):
        return 3.14 * self._radius ** 2


def main():
    new_circle = Circle(5)
    print("Area:", new_circle.get_area())

if __name__ == "__main__":
    main()
