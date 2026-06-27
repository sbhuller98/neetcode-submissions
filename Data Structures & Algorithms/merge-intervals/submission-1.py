class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        ans = []
        intervals.sort()
        prev = intervals[0]
        for i in range(1,len(intervals)):
            interval = intervals[i]

            if interval[0] > prev[1]:
                ans.append(prev)
                prev = interval
            else:
                prev = [min(interval[0], prev[0]), max(interval[1], prev[1])]
            
        ans.append(prev)
        return ans
