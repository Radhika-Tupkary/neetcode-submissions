class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort the intervals based on start of each one
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        # 2. 
        result = []
        result.append(sorted_intervals[0]) 

        for interval in sorted_intervals[1:]:
            start, end = interval[0], interval[1]
            if start <= result[-1][1]:
                last_interval = result.pop()
                result.append([last_interval[0], max(last_interval[1], end)])
            else:
                result.append([start,end])
        
        return result
        