class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        resultIndex = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                resultIndex = i + 1
                total = 0

        return resultIndex


        
