import unittest
from main import Solution

class TestAlternateMerge(unittest.TestCase):
    def test_example_1(self):
        flowerBed = [1,0,0,0,1]
        n = 1
        self.assertEqual(Solution.canPlaceFlowers(self, flowerBed, n), True)

    def test_example_2(self):
        flowerBed = [1,0,0,0,1]
        n = 2
        self.assertEqual(Solution.canPlaceFlowers(self, flowerBed, n), False)

if __name__ == '__main__':
    unittest.main()