class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < bestPrice:
                bestPrice = prices[i]
            profit = max(profit, prices[i] - bestPrice)

        return profit