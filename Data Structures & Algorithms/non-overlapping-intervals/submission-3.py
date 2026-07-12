class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        newIntervals = sorted(intervals)

        ans = 0

        i = 1
        while i < len(newIntervals):
            if newIntervals[i][0] < newIntervals[i-1][1]:
                ans += 1
                if newIntervals[i][1] > newIntervals[i-1][1]:
                    del newIntervals[i]
                else:
                    del newIntervals[i-1]
            else:
                i += 1

        return ans

