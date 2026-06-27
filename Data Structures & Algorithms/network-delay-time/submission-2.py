from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = defaultdict(list)
        for time in times:
            adjacency[time[0]].append((time[1], time[2]))
        heap = []
        heapq.heappush(heap, (0, k))

        seen = set()

        while heap:
            dist, node = heapq.heappop(heap)
            if node in seen:
                continue

            seen.add(node)

            if len(seen) == n:
                return dist
        
            if node in adjacency:
                for adj in adjacency[node]:
                    heapq.heappush(heap, (dist + adj[1], adj[0]))
        
        return -1

            

