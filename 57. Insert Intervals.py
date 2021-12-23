class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Special cases
        if not len(intervals):
            return [newInterval]
        
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        output, index = [], 0
        # Add non-overlapping intervals before
        while index < len(intervals) and newInterval[0] > intervals[index][1]:
            output.append(intervals[index])
            index += 1
        
        # Add overlapping intervals
        start = min(newInterval[0], intervals[index][0])
        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            index += 1
        
        end = max(newInterval[1], intervals[index-1][1])
        output.append([start,end])
        
        # Add non-overlapping intervals after
        for i in range(index, len(intervals)):
            output.append(intervals[i])
        
        return output
