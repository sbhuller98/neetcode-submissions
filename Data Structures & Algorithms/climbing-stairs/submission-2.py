class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {0:1,1:1,2:2}

        def recurse(num):
            if num in memory:
                return memory[num]

            memory[num] = recurse(num - 1) + recurse(num - 2)
            
            return memory[num]
        
        return recurse(n)