class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervalMerged = False

        i = 0
        
        while i < len(intervals):
            prev = intervals[i - 1]
            interval = intervals[i]

            if newIntervalMerged:
                if prev[1] >= interval[0]:
                    interval[0] = min(interval[0], prev[0])
                    interval[1] = max(interval[1], prev[1])
                    intervals.remove(prev)
                    i -= 1
                else:
                    return intervals

            elif interval[0] > newInterval[1]:
                i = intervals.index(interval)
                intervals.insert(i, newInterval)
                return intervals

            elif interval[1] >= newInterval[0]:
                interval[0] = min(interval[0], newInterval[0])
                interval[1] = max(interval[1], newInterval[1])
                newIntervalMerged = True

            elif interval == intervals[-1] and not newIntervalMerged:
                intervals.append(newInterval)
                return intervals
            
            prev = interval
            i += 1

        if intervals:
            return intervals

        return [newInterval]
