import unittest
from calc import *

class TestCalc(unittest.TestCase):
    
    def test_circleS(self):
        self.assertEqual(circleS(3),28.273500000000002)

    def test_triangleS(self):
        test_data = {
            (3, 4, 5, ): 6,
            (145, 105, 100, ): 5250,
            (70, 130, 110, ): 3849.9188303131796,
        }
        for numbers, result in test_data.items():
            self.assertEqual(triangleS(*numbers), result)

    def test_triangleR(self):
        test_data = {
            (3, 4, 5, ): True,
            (145, 105, 100, ): True,
            (70, 130, 110, ): False,
        }
        for numbers, result in test_data.items():
            self.assertEqual(triangleR(*numbers), result)

    
if __name__ == "__main__":
    unittest.main()
