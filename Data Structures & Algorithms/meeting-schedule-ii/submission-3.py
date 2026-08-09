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

        points = []
        for interval in intervals:
            points.append((interval.start, "s"))
            points.append((interval.end, "e"))

        points.sort(key=lambda x: (x[0], 0 if x[1] == 'e' else 1))
        count, maxCount = 0, 0
        
        for point, marker in points:
            if marker == "s":
                count += 1
            else:
                count -= 1

            maxCount = max(count, maxCount)

        return maxCount

