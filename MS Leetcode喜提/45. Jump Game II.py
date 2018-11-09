



# 48ms, 23.31%
# 44ms, 30.31%
from collections import deque
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        queue = deque([[0,0]])
        visited = [False] * len(nums)
        while queue:
            curr, step = queue.popleft()
            for i in xrange(min(len(nums), curr + nums[curr] + 1) - 1, curr, - 1):
                if i == len(nums) - 1:
                    return step + 1
                elif not visited[i]:
                    visited[i] = True
                    queue.append([i,step + 1])
        return -1