class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest = None
        l,r = 1, 1000000000

        while l <= r:
            m = (l + r) // 2

            totalHours = 0

            for item in piles:
                totalHours += -(-item // m)
            
            if totalHours <= h:
                if not lowest or lowest > m:
                    lowest = m
                r = m - 1
            else:
                l = m + 1

        return lowest