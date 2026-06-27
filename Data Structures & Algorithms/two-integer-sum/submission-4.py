from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            curr = target - num
            if curr in dictionary:
                return [dictionary[curr], i]
            dictionary[num] = i

        return []