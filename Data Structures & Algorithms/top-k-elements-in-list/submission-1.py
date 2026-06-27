from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory = [[] for i in range(len(nums) + 1)]
        dictionary = defaultdict(int)

        for num in nums:
            dictionary[num] += 1

        for key,v in dictionary.items():
            memory[v].append(key)

        ans = []
        for i in range(len(memory) - 1, 0, -1):
            for item in memory[i]:
                ans.append(item)
                if len(ans) == k:
                    return ans
