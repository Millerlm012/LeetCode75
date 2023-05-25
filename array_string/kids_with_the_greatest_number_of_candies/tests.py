import unittest
from main import FirstSolution, SecondSolution, ThirdSolution

class TestAlternateMerge(unittest.TestCase):
    def test_example_1(self):
        candies = [2,3,5,1,3]
        extraCandies = 3
        result = [True,True,True,False,True]
        self.assertEqual(FirstSolution.kidsWithCandies(self, candies, extraCandies), result)
        self.assertEqual(SecondSolution.kidsWithCandies(self, candies, extraCandies), result)
        self.assertEqual(ThirdSolution.kidsWithCandies(self, candies, extraCandies), result)

    def test_example_2(self):
        candies = [4,2,1,1,2]
        extraCandies = 1
        result = [True,False,False,False,False] 
        self.assertEqual(FirstSolution.kidsWithCandies(self, candies, extraCandies), result)
        self.assertEqual(SecondSolution.kidsWithCandies(self, candies, extraCandies), result)
        self.assertEqual(ThirdSolution.kidsWithCandies(self, candies, extraCandies), result)

    def test_example_3(self):
        candies = [12,1,12]
        extraCandies = 10
        result = [True,False,True]
        self.assertEqual(FirstSolution.kidsWithCandies(self, candies, extraCandies), result)
        self.assertEqual(SecondSolution.kidsWithCandies(self, candies, extraCandies), result)
        self.assertEqual(ThirdSolution.kidsWithCandies(self, candies, extraCandies), result)

if __name__ == '__main__':
    unittest.main()