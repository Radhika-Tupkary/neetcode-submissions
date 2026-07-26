class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort the intervals based on start of each one
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        # 2. Keep 
        result = []
        result.append(sorted_intervals[0]) 

        for currentStart, currentEnd in sorted_intervals:
            if currentStart <= result[-1][1]:
                last_interval = result.pop()
                result.append([last_interval[0], max(last_interval[1], currentEnd)])
            else:
                result.append([currentStart, currentEnd])
        
        return result
        