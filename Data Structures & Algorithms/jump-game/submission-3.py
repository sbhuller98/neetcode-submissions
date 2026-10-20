class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = len(nums) - 1
        jumpsNeeded = 0
        while i >= 0:
            if nums[i] >= jumpsNeeded:
                jumpsNeeded = 1
            else:
                jumpsNeeded += 1
            i -= 1

        if jumpsNeeded == 1:
            return True

        return False

