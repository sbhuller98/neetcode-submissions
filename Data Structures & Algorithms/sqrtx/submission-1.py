class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x

        while l < r:
            m = (l + r) // 2
            val = m ** 2
            print(val)
            if val == x:
                return m
            elif val > x:
                r = m - 1
            else:
                if ((m + 1) ** 2) > x:
                    return m
                l = m + 1
            
        
        return l