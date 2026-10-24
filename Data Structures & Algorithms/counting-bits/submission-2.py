class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            k = i
            while k:
                ans[i] += 1
                k &= (k-1)

        return ans