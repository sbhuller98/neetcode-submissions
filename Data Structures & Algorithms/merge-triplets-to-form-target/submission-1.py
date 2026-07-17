class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [0,0,0]
        
        for trip in triplets:
            earlyCancel = False
            for i in range(len(trip)):
                if trip[i] > target[i]:
                    earlyCancel = True
                    break
                if trip[i] == target[i]:
                    match[i] = 1
            
            if not earlyCancel and sum(match) == 3:
                    return True

        return False
