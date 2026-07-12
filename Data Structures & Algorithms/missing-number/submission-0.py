class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0

        for i in range(1, len(nums)+ 1):
            total += i

        for item in nums:
            total -= item

        return total