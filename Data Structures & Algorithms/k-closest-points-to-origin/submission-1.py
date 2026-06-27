from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsHeap = []
        for item in points:
            val = item[0] ** 2 + item[1] ** 2
            heapq.heappush_max(pointsHeap, [val, item[0], item[1]])
            if len(pointsHeap) > k:
                heapq.heappop_max(pointsHeap)

        ans = []
        while pointsHeap:
            val = heapq.heappop(pointsHeap)
            ans.append([val[1], val[2]])
        
        return ans
            
        
