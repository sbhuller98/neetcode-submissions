class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        maxSoFar = 0

        for num in nums:
            i = 1
            iteration = 1
            while True:
                if num + i not in unique:
                    break
                i += 1
                iteration += 1
            maxSoFar = max(maxSoFar, iteration)
        
        return maxSoFar