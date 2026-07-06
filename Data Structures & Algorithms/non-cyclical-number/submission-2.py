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
            for ch in str(curr):
                total += int(ch) ** 2
            curr = total
            
            