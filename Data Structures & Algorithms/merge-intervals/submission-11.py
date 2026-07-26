class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort the intervals based on start of each one
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        # 2. Keep comparing intervals and check for overlap. If overlap ---> update, else ---> append.
        result = []
        result.append(sorted_intervals[0]) 

        for currentStart, currentEnd in sorted_intervals:
            if currentStart <= result[-1][1]:
                lastStart, lastEnd = result.pop()
                result.append([lastStart, max(lastEnd, currentEnd)])
            else:
                result.append([currentStart, currentEnd])
        
        return result
        