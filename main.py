import math

class Square():
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2
    
    def calculate_perimeter(self):
        return 4*self.side

class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.width = x1 - x2
        self.height = y1 - y2

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
        

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi

    def calculate_area(self):
        return int((self.radius**2) * self.pi)
    
    def calculate_perimeter(self):
        return int(2 * self.pi * self.radius)


def match_shape(a):
    match a.split(" "):
        case ['Square', *a]:
            square = Square(int(a[-1]))
            return f'Square Perimeter {square.calculate_perimeter()} Area {square.calculate_area()}'
        case ['Rectangle', *a]:
            rectangle = Rectangle(int(a[1]), int(a[2], int(a[-1], int(a[-2]))))
            return f"Rectangle Perimeter {rectangle.calculate_perimeter()} Area {rectangle.calculate_areat()}"
        case ['Circle', *a]:
            circle = Circle(int(a[-1]))
            return f"Circle Perimeter {circle.calculate_perimeter()} Area {circle.calculate_area()}"
        case _:
            print("You have entered a shape that is not supported by the program code")

if __name__ == "__main__":
    a = input("Enter data about geometric shapes using the example. Shape type Description of parameters: for example, for a square it can be TopRight, Side, for a rectangle - TopRight, BottomLeft, and for a circle - Center and Radius: \n")
    print(match_shape(a))
