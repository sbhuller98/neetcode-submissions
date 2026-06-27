class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = None
        total = 0 
        for price in prices:
            if lowest is None:
                lowest = price
            else:
                if price > lowest:
                    total += (price - lowest)
                lowest = price
        return total