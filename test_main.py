import unittest
from main import *

class ShapeCalculateTest(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square("TopRight 1 1 Side 1".split(" ")), "Square Perimeter 4 Area 1")

    def test_rectangle(self):
        self.assertEqual(rectangle("TopRight 2 2 BottomLeft 1 1".split(" ")), "Rectangle Perimeter 4 Area 1")

    def test_circle(self):
        self.assertEqual(circle("Center 1 1 Radius 2".split(" ")), "Circle Perimeter 1 Area 2")

if __name__ == "__main__":
    unittest.main()

