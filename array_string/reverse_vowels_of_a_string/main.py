"""
Merge Strings Alternately: Completed on 2023-05-26
Problem: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
"""

class FirstSolution:
    def reverseVowels(self, s: str) -> str:
        indexes = []
        found_vowels = []
        for i, letter in enumerate(s):
            if letter.lower() in 'aeiou':
                indexes.append(i)
                found_vowels.append(letter)

        found_vowels.reverse()
        for i, vowel in enumerate(found_vowels):
            s = s[:indexes[i]] + vowel + s[indexes[i] + 1:]

        return s

class SecondSolution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        chars = list(s)
        l = 0
        r = len(chars) - 1
        while l < r:
            while l < r and chars[l].lower() not in vowels:
                l += 1
            while l < r and chars[r].lower() not in vowels:
                r -= 1
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1

        return ''.join(chars)