from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = defaultdict(list)
        pointsHeap = []
        for item in points:
            val = item[0] ** 2 + item[1] ** 2
            store[val].append(item)
            heapq.heappush(pointsHeap, val)

        ans = []
        while len(ans) < k:
            val = heapq.heappop(pointsHeap)
            ans.append(store[val].pop())
        
        return ans
            
        
