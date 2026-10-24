class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = float('-inf')
        curr = 0

        for num in nums:
            curr += num
            maxSoFar = max(maxSoFar, curr)
            if curr < 0:
                curr = 0

        return maxSoFar