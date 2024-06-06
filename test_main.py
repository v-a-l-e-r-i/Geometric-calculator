import unittest
from main import *

class ShapeCalculateTest(unittest.TestCase):
    
    def test_shapes(self):
        outpu_list = ['Square Perimeter 4 Area 1', 'Rectangle Perimeter 4 Area 1', 'Circle Perimeter 12 Area 12']

        self.assertEqual(generate_output("Square TopRight 1 1 Side 1\nRectangle TopRight 2 2 BottomLeft 1 1\nCircle Center 1 1 Radius 2"), outpu_list)

if __name__ == "__main__":
    unittest.main()

