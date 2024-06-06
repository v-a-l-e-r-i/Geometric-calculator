import math

class Shape():
    def __init__(self, shape_type, topRight=None, topLeft=None, bottomRight=None, bottomLeft=None, center=None):
        self.shape_type = shape_type


class Square(Shape):
    def __init__(self, side, topRight=None):
        super().__init__('Square', topRight)
        self.side = side

    def calculate_area(self):
        return self.side**2
    
    def calculate_perimeter(self):
        return 4*self.side

class Rectangle(Shape):
    def __init__(self, topRight, bottomLeft):
        super().__init__('Rectangle', topRight, bottomLeft)
        self.width = topRight[0] - bottomLeft[0]
        self.height = topRight[1] - bottomLeft[1]

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
        

class Circle(Shape):
    def __init__(self, radius, center=None):
        super().__init__('Circle', center)
        self.radius = radius

    def calculate_area(self):
        return int((self.radius**2) * math.pi)
    
    def calculate_perimeter(self):
        return int(2 * math.pi * self.radius)


def match_shape(line):
    line = line.strip()
    print(line)
    match line.split(" "):
        case ['Square', *a]:
            square = Square(int(a[-1]), (a[1], a[2]))
            return f'{square.shape_type.title()} Perimeter {square.calculate_perimeter()} Area {square.calculate_area()}'
        case ['Rectangle', *a]:
            rectangle = Rectangle((int(a[1]), int(a[2])), (int(a[-1]), int(a[-2])))
            return f"{rectangle.shape_type.title()} Perimeter {rectangle.calculate_perimeter()} Area {rectangle.calculate_area()}"
        case ['Circle', *a]:
            circle = Circle(int(a[-1]), (a[1], a[2]))
            return f"{circle.shape_type.title()} Perimeter {circle.calculate_perimeter()} Area {circle.calculate_area()}"
        case _:
            print("You have entered a shape that is not supported by the program code")

def generate_output(lines):
    output = []
    lines = lines.strip()
    for line in lines.split("\n"):
        output.append(match_shape(line))
    return output
    


if __name__ == "__main__":
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    lines = ""
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines += line + "\n"
    print(generate_output(lines))


