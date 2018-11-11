

# Heap solution: O(nlogn)
from heapq import heappush, heappop
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k <= 1: return nums
        if k == len(nums): return [max(nums)]

        res = []
        heap = []
        for i in xrange(len(nums)):
            if i < k - 1:
                heappush(heap, [-nums[i], i])
            else:
                start = i - k
                if nums[i] > -heap[0][0]:
                    heappush(heap, [-nums[i], i])
                    res.append(-heap[0][0])
                else:
                    while len(heap) >= k and heap[0][1] <= start:
                        heappop(heap)
                    heappush(heap, [-nums[i], i])
                    res.append(-heap[0][0])
        return res
