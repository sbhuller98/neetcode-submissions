import heapq
from collections import defaultdict
class Solution:
    def manHattanD(self,p1, p2):
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, points[0][0], points[0][1])]
        adj = defaultdict(list)
        ans = 0

        for i in range(len(points)):
            for j in range(len(points)):
                adj[(points[i][0], points[i][1])].append((self.manHattanD(points[i], points[j]), points[j][0], points[j][1]))

        seen = set()
        while heap and len(seen) < len(points):
            dist,x,y = heapq.heappop(heap)
            if (x,y) in seen:
                continue
            ans += dist
            seen.add((x,y))
            for item in adj[(x,y)]:
                if (item[1], item[2]) not in seen:
                    heapq.heappush(heap,item)

        return ans