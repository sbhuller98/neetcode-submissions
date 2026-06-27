class MedianFinder:

    def __init__(self):
        self.heapLeft = []
        self.heapRight = []

    def addNum(self, num: int) -> None:
        if not self.heapLeft:
            heapq.heappush_max(self.heapLeft, num)
        elif num < self.heapLeft[0]:
            heapq.heappush_max(self.heapLeft, num)
            if len(self.heapLeft) - len(self.heapRight) > 1:
                val = heapq.heappop_max(self.heapLeft)
                heapq.heappush(self.heapRight, val)
        else:
            heapq.heappush(self.heapRight, num)
            if len(self.heapRight) - len(self.heapLeft) > 1:
                val = heapq.heappop(self.heapRight)
                heapq.heappush_max(self.heapLeft, val)

    def findMedian(self) -> float:
        if len(self.heapLeft) == len(self.heapRight):
            return (self.heapLeft[0] + self.heapRight[0]) / 2
        elif len(self.heapLeft) > len(self.heapRight):
            return self.heapLeft[0]
        else:
            return self.heapRight[0]
        