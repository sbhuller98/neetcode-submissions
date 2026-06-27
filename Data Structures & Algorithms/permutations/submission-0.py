class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recurse(curr, seen):
            if len(seen) == len(nums):
                ans.append(curr.copy())
                return
            for item in nums:
                if item in seen:
                    continue
                curr.append(item)
                seen.add(item)
                recurse(curr, seen)
                curr.pop()
                seen.remove(item)
        
        recurse([], set())
        return ans