class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        arr = [0] * (len(cost))

        arr[0] = cost[0]
        arr[1] = cost[1]

        for i in range(2, len(cost)):
            arr[i] = min(arr[i-1], arr[i-2]) + cost[i]

        return min(arr[-1], arr[-2])
