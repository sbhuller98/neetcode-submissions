class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for item in nums:
            heapq.heappush(minHeap, item)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
        
