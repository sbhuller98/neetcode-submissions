class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * (len(cost))
        prevTwo = cost[0]
        prevOne = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prevOne, prevTwo)
            prevTwo = prevOne
            prevOne = curr


        return min(prevOne, prevTwo)
