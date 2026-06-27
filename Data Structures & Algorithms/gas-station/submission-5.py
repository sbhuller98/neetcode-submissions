class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        resultIndex = 0
        total = 0
        fullTotal = 0
        for i in range(len(gas)):
            curr = gas[i] - cost[i]
            total += curr
            fullTotal += curr
            if total < 0:
                resultIndex = i + 1
                total = 0

        if fullTotal >= 0:
            return resultIndex
        return -1


        
