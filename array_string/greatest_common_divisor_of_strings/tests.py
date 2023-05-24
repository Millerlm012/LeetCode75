import unittest
from main import Solution

class TestGreatCommonDivisor(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution.gcdOfStrings(self, 'ABCABC', 'ABC'), 'ABC')

    def test_example_2(self):
        self.assertEqual(Solution.gcdOfStrings(self, 'ABABAB', 'ABAB'), 'AB')

    def test_example_3(self):
        self.assertEqual(Solution.gcdOfStrings(self, 'LEET', 'CODE'), '')

if __name__ == '__main__':
    unittest.main()