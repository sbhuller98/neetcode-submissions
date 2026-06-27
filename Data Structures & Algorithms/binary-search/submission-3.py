class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        rb = len(nums) -1

        while lb != rb and lb > -1 and rb > -1:
            mid = (lb + rb) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rb = mid - 1
            else:
                lb = mid + 1

        return lb if lb > -1 and nums[lb] == target else -1