from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        limit = len(nums) // 2 + 1

        for item in nums:
            seen[item] += 1
            if seen[item] == limit:
                return item
    