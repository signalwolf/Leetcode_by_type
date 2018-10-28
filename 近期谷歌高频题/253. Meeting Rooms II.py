# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort(key = lambda x:x.start)
        heap = []
        res = 0
        for interval in intervals:
            if len(heap) >0 and interval.start >= heap[0]:
                heappop(heap)
            heappush(heap, interval.end)
            res = max(res, len(heap))
        return res