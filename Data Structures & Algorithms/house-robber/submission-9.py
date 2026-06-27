class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        val2 = 0
        val1 = 0

        for i in range(len(nums)):
            tmp = val1
            val1 = max(nums[i] + val2, val1)
            val2 = tmp


        return max(val1,val2)
