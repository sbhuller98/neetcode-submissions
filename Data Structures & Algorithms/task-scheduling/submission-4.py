from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)

        for item in tasks:
            counts[item] += 1

        quantity = 0
        maxSoFar = 0

        for k,v in counts.items():
            if v > maxSoFar:
                maxSoFar = v
                quantity = 1
            elif v == maxSoFar:
                quantity += 1
        
        return max((maxSoFar - 1) * n + (quantity - 1) + maxSoFar, len(tasks))


                
            
        



        
