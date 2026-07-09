class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        carry = 0

        for num in nums:
            carry ^= num

        return carry
        