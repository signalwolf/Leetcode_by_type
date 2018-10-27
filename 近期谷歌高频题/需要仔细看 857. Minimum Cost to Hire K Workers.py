# coding=utf-8
# 解法一： 以每一个worker都作为锚点，然后将能满足当前ratio的worker都加入到一个表里面
# 然后sort 表后取前 K 个。
# run out of time
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        q, w, r = 0, 1, 2
        ratio = [wage[i] / float(quality[i]) for i in xrange(len(wage))]
        total_cost = float('inf')
        combined = zip(quality, wage, ratio)
        # combined.sort(key = lambda x:x[2])
        for i in xrange(len(quality)):
            base = combined[i][r]
            curr_cost = []
            # hired_worker = 0
            for j in xrange(len(quality)):
                if base * combined[j][q] >= combined[j][w]:
                    curr_cost.append(base * combined[j][q])
            if len(curr_cost) >= K:
                total_cost = min(total_cost, sum(sorted(curr_cost)[:K]))
        return total_cost

# 解法一是over kill了这个问题，毕竟是不需要去sort它的。那么要怎么保持呢？
# heap可以解决这个问题，每次我们都pop掉quality 最大的那个。

from heapq import heappush, heappop
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        q, w, r = 0, 1, 2
        ratio = [wage[i] / float(quality[i]) for i in xrange(len(wage))]
        total_cost = float('inf')
        combined = zip(quality, wage, ratio)
        # combined.sort(key = lambda x:x[2])
        for i in xrange(len(quality)):
            base = combined[i][r]
            curr_cost = []
            # hired_worker = 0
            for j in xrange(len(quality)):
                if base * combined[j][q] >= combined[j][w]:
                    heappush(curr_cost, -(base * combined[j][q]))

                if len(curr_cost) > K:
                    heappop(curr_cost)

            if len(curr_cost) == K:
                total_cost = min(total_cost, sum(curr_cost) * - 1)
        return total_cost


# 最后的最优的解法就需要一点思考了，如果我们sort wokers based on wage/quality, 那么低的ratio在前，
# 故而高的ratio在后面被分析的时候前面的低ratio的worker一定满足条件。ratio[i] * quality[j] (j < i)
# 一定大于wage[j].
# 也就是说对于当下的worker来说，能满足它条件的都在它前面。故而使用一个heap就能解决问题。

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
