from heapq import heappush, heappop


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < k: return -1
        pq = []
        for num in nums:
            heappush(pq, num)
            if len(pq) == k + 1:
                heappop(pq)
        return pq[0]