class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        lowest = r

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