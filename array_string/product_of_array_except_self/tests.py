import unittest
from main import FirstSolution, SecondSolution

class TestAlternateMerge(unittest.TestCase):
    def test_example_1(self):
        nums = [1,2,3,4]
        result = [24,12,8,6]
        self.assertEqual(FirstSolution.productExceptSelf(self, nums), result)
        self.assertEqual(SecondSolution.productExceptSelf(self, nums), result)

    def test_example_2(self):
        nums = [-1,1,0,-3,3]
        result = [0,0,9,0,0]
        self.assertEqual(FirstSolution.productExceptSelf(self, nums), result)
        self.assertEqual(SecondSolution.productExceptSelf(self, nums), result)

if __name__ == '__main__':
    unittest.main()