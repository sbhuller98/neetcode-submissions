import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if len(flights) < 2:
            return -1
        
        graph = defaultdict(list)

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        heap = []

        for fl in graph[src]:
            heapq.heappush(heap, (fl[1], 0, src, fl[0])) 

        total = float('inf')
        pathSoFar = []
        seen = set()

        while heap:
            cost, stops, start, end = heapq.heappop(heap)
            if stops > k:
                continue
            if end == dst:
                return cost

            print(stops)
            
            for fl in graph[end]:
                if fl[0] == start:
                    continue
                heapq.heappush(heap, (cost + fl[1], stops + 1, end, fl[0]))

        return -1




            


        