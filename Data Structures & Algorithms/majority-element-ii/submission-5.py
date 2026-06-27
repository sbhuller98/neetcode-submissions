from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        memory = defaultdict(int)

        for num in nums:
            memory[num] += 1

            if len(memory) > 2:
                new_count = defaultdict(int)
                for k, c in memory.items():
                    if c > 1:
                        new_count[k] = c - 1
                memory = new_count
            
        res = []
        for num in memory:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res
                    