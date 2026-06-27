class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = stones
        heapq.heapify_max(stonesHeap)

        while len(stonesHeap) > 1:
            st1 = heapq.heappop_max(stonesHeap)
            st2 = stonesHeap[0]
            if st1 == st2:
                heapq.heappop_max(stonesHeap)
            elif st1 > st2:
                heapq.heapreplace_max(stonesHeap, st1 - st2)
            else:
                heapq.heapreplace_max(stonesHeap, st2 - st1)

        return stonesHeap[0] if stonesHeap else 0