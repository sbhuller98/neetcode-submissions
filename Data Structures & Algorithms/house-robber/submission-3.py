class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(max(nums), nums[0] + nums[2])
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = nums[1]
        arr[2] = max(nums[1], nums[0] + nums[2])

        for i in range(2, len(nums)):
            arr[i] = max(arr[i-2], arr[i-3]) + nums[i]

        return max(arr)

            