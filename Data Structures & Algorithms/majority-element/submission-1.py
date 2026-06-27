from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = count = 0

        for item in nums:
            if count == 0:
                target = item
            if item == target:
                count += 1
            else:
                count -= 1
        
        return target
    