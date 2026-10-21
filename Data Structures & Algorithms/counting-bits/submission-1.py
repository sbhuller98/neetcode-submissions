class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            k = i
            for j in range(k // 2 + 1):
                if i & 1:
                    count += 1
                i = i >> 1
            ans.append(count)

        return ans