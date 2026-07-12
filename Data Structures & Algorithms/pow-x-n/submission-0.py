class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n > 0:
            ans = x
            for i in range(n-1):
                ans *= x
            return ans
        else:
            ans = 1/x
            for i in range(abs(n) - 1):
                print(ans)
                ans *= 1/x
            return ans
