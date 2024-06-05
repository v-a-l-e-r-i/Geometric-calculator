import unittest
from main import *

class ShapeCalculateTest(unittest.TestCase):
    def test_square(self):
        self.assertEqual(match_shape("Square TopRight 1 1 Side 1"), "Square Perimeter 4 Area 1")

    def test_rectangle(self):
        self.assertEqual(match_shape("Rectangle TopRight 2 2 BottomLeft 1 1"), "Rectangle Perimeter 4 Area 1")

    def test_circle(self):
        self.assertEqual(match_shape("Circle Center 1 1 Radius 2"), "Circle Perimeter 1 Area 2")

if __name__ == "__main__":
    unittest.main()

