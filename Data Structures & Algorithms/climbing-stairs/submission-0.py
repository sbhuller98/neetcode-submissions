class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {0:1,1:1}

        
        def recurse(num):
            if num in memory:
                return memory[num]

            count = 0
            if num >=2:
                twoStepCount = recurse(num-2)
                memory[num-2] = twoStepCount
                count += twoStepCount
            
            if num >= 1:
                oneStepCount = recurse(num-1)
                memory[num-1] = oneStepCount
                count += oneStepCount
            
            return count
        
        return recurse(n)