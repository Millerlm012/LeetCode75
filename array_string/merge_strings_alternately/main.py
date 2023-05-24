"""
Merge Strings Alternately: Completed on 2023-05-22
Problem: https://leetcode.com/problems/merge-strings-alternately/
"""

class FirstSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        iterations = 0
        if len(word1) > len(word2):
            iterations = len(word1)
        else:
            iterations = len(word2)

        for i in range(iterations):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]

        return merged

class SecondSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        count = 0
        while count < max(len(word1), len(word2)):
            if count < len(word1):
                merged += word1[count]

            if count < len(word2):
                merged += word2[count]

            count += 1

        return merged