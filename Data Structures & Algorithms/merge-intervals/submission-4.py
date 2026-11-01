class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        print(intervals)

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] <= ans[-1][1]:
                ans[-1][1] = max(curr[1], ans[-1][1])
            else:
                ans.append(curr)

        return ans