import unittest
from main import FirstSolution, SecondSolution, ThirdSolution

class TestAlternateMerge(unittest.TestCase):
    def test_example_1(self):
        s = "the sky is blue"
        result = "blue is sky the"
        self.assertEqual(FirstSolution.reverseWords(self, s), result)
        self.assertEqual(SecondSolution.reverseWords(self, s), result)
        self.assertEqual(ThirdSolution.reverseWords(self, s), result)

    def test_example_2(self):
        s = "  hello world  "
        result = "world hello"
        self.assertEqual(FirstSolution.reverseWords(self, s), result)
        self.assertEqual(ThirdSolution.reverseWords(self, s), result)

    def test_example_3(self):
        s = "a good   example"
        result = "example good a"
        self.assertEqual(FirstSolution.reverseWords(self, s), result)
        self.assertEqual(ThirdSolution.reverseWords(self, s), result)

if __name__ == '__main__':
    unittest.main()