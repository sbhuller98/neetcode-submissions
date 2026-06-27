class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        store = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            count = 1
            temp = temperatures[i]
            while store and temp > store[-1][1]:
                val = store.pop()
                ans[val[0]] = i - val[0] 
                count += 1
            store.append((i, temp))

        return ans