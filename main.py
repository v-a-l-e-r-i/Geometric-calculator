import math

def square(parameter):
    try:
        a = int(parameter[-1])
        return(f'Square Perimeter {4*a} Area {a**4}')
    except:
        raise TypeError

def rectangle(parameter):
    try:
        xTopRight = int(parameter[1])
        yTopRight = int(parameter[2])
        xBottomLeft = int(parameter[-1])
        yBottomLeft = int(parameter[-2])

        width = xTopRight - xBottomLeft
        height = yTopRight - yBottomLeft

        return (f"Rectangle Perimeter {2 * (width + height)} Area {width * height}")
    except:
        raise TypeError

def circle(parameter):
    try:
        pi = math.pi
        radius = int(parameter[-1])
        return (f"Circle Perimeter {int(2 * pi * radius)} Area {int((radius**2) * pi)}")
    except:
        raise TypeError


def match_shape(a):
    match a.split(" "):
        case ['Square', *files]:
            square(files)
        case ['Rectangle', *files]:
            rectangle(files)
        case ['Circle', *files]:
            circle(files)
        case _:
            print("You have entered a shape that is not supported by the program code")

if __name__ == "__main__":
    a = input("Enter data about geometric shapes using the example. Shape type Description of parameters: for example, for a square it can be TopRight, Side, for a rectangle - TopRight, BottomLeft, and for a circle - Center and Radius: \n")
    match_shape(a)
