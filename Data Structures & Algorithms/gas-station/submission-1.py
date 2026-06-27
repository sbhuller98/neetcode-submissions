class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def isValidPath(start):
            tank = 0
            i = start
            while True:
                tank += gas[i]
                tank -= cost[i]
                if tank < 0:
                    return False
                
                i += 1

                if i == len(gas):
                    i = 0
                if i == start:
                    return True


        stationsToCheck = []

        for i in range(0, len(gas)):
            if gas[i] >= cost[i]:
                stationsToCheck.append(i)

        stationsToCheck.sort(reverse=True)

        for st in stationsToCheck:
            if isValidPath(st):
                return st

        return -1

        
