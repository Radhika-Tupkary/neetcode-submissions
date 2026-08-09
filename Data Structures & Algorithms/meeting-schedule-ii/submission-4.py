"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda x:x.start)
        # min_heap = []
        
        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)

        #     heapq.heappush(min_heap, interval.end)

        # return len(min_heap)

        starts = [interval.start for interval in intervals]
        starts.sort()
        ends = [interval.end for interval in intervals]
        ends.sort()
        s, e, count, maxCount = 0, 0, 0, 0
        
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            
            maxCount = max(count, maxCount)


        return maxCount 

