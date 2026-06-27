class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                if i - l > 1 and nums[i] != nums[i-1]:
                    nums[l+1] = nums[i]
                l += 1

            i += 1

        return l + 1