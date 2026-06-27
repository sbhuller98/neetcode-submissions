class Solution:
    def canJump(self, nums: List[int]) -> bool:
        carry = 0

        for i in range(len(nums) - 1, -1, -1):
                if nums[i] >= carry:
                    carry = 0
                carry += 1

        if carry == 1:
            return True
        return False