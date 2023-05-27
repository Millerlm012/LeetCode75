from typing import List

# O(n^2) - question states that it's wanting O(n) though
class FirstSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = 0
        result = []
        while counter < len(nums):
            product = 1
            for i, num in enumerate(nums):
                if i != counter:
                    product = product * num
            result.append(product)
            counter += 1
        
        return result

class SecondSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result