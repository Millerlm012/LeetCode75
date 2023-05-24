import unittest
from main import FirstSolution, SecondSolution

class TestAlternateMerge(unittest.TestCase):
    def test_example_1(self):
        word1 = 'abc'
        word2 = 'pqr'
        self.assertEqual(FirstSolution.mergeAlternately(self, word1, word2), 'apbqcr')
        self.assertEqual(SecondSolution.mergeAlternately(self, word1, word2), 'apbqcr')

    def test_example_2(self):
        word1 = 'ab'
        word2 = 'pqrs'
        self.assertEqual(FirstSolution.mergeAlternately(self, word1, word2), 'apbqrs')
        self.assertEqual(SecondSolution.mergeAlternately(self, word1, word2), 'apbqrs')

    def test_example_3(self):
        word1 = 'abcd'
        word2 = 'pq'
        self.assertEqual(FirstSolution.mergeAlternately(self, word1, word2), 'apbqcd')
        self.assertEqual(SecondSolution.mergeAlternately(self, word1, word2), 'apbqcd')

if __name__ == '__main__':
    unittest.main()