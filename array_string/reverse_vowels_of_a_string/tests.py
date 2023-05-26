import unittest
from main import FirstSolution, SecondSolution

class TestAlternateMerge(unittest.TestCase):
    def test_example_1(self):
        input = 'hello'
        output = 'holle'
        self.assertEqual(FirstSolution.reverseVowels(self, input), output)
        self.assertEqual(SecondSolution.reverseVowels(self, input), output)

    def test_example_2(self):
        input = 'leetcode'
        output = 'leotcede'
        self.assertEqual(FirstSolution.reverseVowels(self, input), output)
        self.assertEqual(SecondSolution.reverseVowels(self, input), output)

if __name__ == '__main__':
    unittest.main()