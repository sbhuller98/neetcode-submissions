class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        best = -math.inf

        for i in range(len(nums)):
            if total <= 0:
                total = nums[i]
            else:
                total += nums[i]
                
            

            best = max(total, nums[i], best)
        
        return best