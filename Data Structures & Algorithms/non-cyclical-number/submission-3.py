class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n

        while True:
            if curr == 1:
                return True
            if curr in seen:
                return False

            total = 0
            seen.add(curr)
            while curr > 0:
                total += (curr % 10) ** 2
                curr //= 10
            curr = total
            
            