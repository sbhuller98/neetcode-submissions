class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        maxTwo = nums[0]
        maxOne = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(maxOne, nums[i] + maxTwo)
            maxTwo = maxOne
            maxOne = curr

        return maxOne
   