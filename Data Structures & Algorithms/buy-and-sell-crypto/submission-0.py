class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[R] - prices[L] > profit:
                profit = prices[R] - prices[L]
            if prices[R] < prices[L]:
                L = R
            R += 1
        
        return profit