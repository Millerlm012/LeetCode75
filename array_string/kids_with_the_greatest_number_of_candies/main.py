"""
Merge Strings Alternately: Completed on 2023-05-24
Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""
from typing import List

class FirstSolution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)

        return results

class SecondSolution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if candy + extraCandies >= max(candies) else False for candy in candies]

class ThirdSolution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        max_candy = 0
        for candy in candies:
            if candy > max_candy:
                max_candy = candy

        for candy in candies:
            if candy + extraCandies >= max_candy:
                results.append(True)
            else:
                results.append(False)

        return results