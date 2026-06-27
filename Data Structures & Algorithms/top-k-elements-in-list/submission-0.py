from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory = defaultdict(int)

        for num in nums:
            memory[num] += 1

        final = list(key for key,v in sorted(memory.items(), key=lambda item: item[1], reverse = True))
        return final[0:k]