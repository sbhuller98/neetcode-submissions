class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def recurse(curr, index):
            ans.append(curr.copy())
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
        
                curr.append(nums[i])
                recurse(curr, i + 1)
                curr.pop()
        
        recurse([], 0)
        return ans
            