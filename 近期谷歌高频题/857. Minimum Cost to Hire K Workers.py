# coding=utf-8
# 

from heapq import heappush, heappop
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted([wage[i] / float(quality[i]), quality[i], wage[i]] for i in range(len(quality)))

        res, pool, sum_pool = float('inf'), [], 0
        for ratio, quality, wage in workers:
            heappush(pool, -quality)
            sum_pool += quality

            if len(pool) == K + 1:
                sum_pool += heappop(pool)
            if len(pool) == K:
                res = min(res, sum_pool * ratio)
        return res
