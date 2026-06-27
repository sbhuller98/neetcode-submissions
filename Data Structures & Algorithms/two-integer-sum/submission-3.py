from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(list)

        for i, item in (enumerate(nums)):
            hashMap[item].append(i)

        for i, item in enumerate(nums):
            curr = target - item
            if curr in hashMap:
                for num in hashMap[curr]:
                    if num != i:
                        ans = [i, num]
                        ans.sort()
                        return ans

        return []