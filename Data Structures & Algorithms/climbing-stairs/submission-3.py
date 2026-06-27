class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        oneStep = 2
        twoStep = 1

        for i in range(3, n + 1):
            curr = oneStep + twoStep
            twoStep = oneStep
            oneStep = curr
            
        
        return oneStep