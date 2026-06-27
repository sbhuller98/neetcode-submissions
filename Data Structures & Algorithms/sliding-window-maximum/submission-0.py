from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        store = SortedList(nums[0:k-1])
        ans = []
        
        for i in range(k-1, len(nums)):
            store.add(nums[i])
            ans.append(store[-1])
            store.remove(nums[i - k + 1])
        
        return ans
