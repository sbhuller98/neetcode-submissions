class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j = 0 , len(nums) - 1
        
        while i <= j:
            mid = (i + j) // 2

            if (mid > 0 and nums[mid] < nums[mid - 1]):
                i = mid 
                break

            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid -1

        return nums[i]

    

            