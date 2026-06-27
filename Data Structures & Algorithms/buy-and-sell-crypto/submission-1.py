class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L, R = 0, 1

        while R < len(prices):
            profit = max(prices[R] - prices[L], profit)
            if prices[R] < prices[L]:
                L = R
            R += 1
        
        return profit