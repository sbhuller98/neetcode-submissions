class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = (l + r) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                r = midpoint - 1
                
        return l