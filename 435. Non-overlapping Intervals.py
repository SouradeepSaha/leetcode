class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = 0
        lastInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastInterval[1]:
                result += 1
                lastInterval = lastInterval if lastInterval[1] < intervals[i][1] else intervals[i]
            else:
                lastInterval = intervals[i]
        
        return result
