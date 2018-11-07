# coding=utf-8

# 需要稍微思考一下答案：
#   1. 首先最重要的是题目说了只有一个解或者没有解
#   2. 故而首先：如果 sum(gas) < sum(cost), 那就是没有解
#   3. 然后如果从一个点出发，中间遇到了小于零的情况，那么出发点到小于零点之间的点都不是answer，所以可以直接skip
#   4. 这时候reset everything: balance = 0, i = i + 1
#   5. 重新search 就好

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1

        balance = 0
        res = 0
        for i in xrange(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                res = i + 1
        return res
