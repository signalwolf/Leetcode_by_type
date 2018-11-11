from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 0 or k == 1:
            return nums
        queue = deque([])
        res = []
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        for i in range(k, len(nums)):
            res.append(nums[queue[0]])
            if i - queue[0] >= k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        return res