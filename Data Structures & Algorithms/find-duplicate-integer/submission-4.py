from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = None
        for num in nums:
            if nums[abs(num) - 1] < 0:
                if num < 0:
                    ans = -num
                else:
                    ans = num
                break
            
            nums[abs(num) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -(nums[i])
        
        return ans