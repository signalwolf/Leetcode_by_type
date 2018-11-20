# coding=utf-8

# 刚开始使用的是 4 in dists.values().
# 后来发现不对，其实如果是square的话， 总共6条线，那么应该是4条长度一样，2条场地一样，这样才算对

from collections import defaultdict
class Solution(object):

    def calcDist(self, node1, node2):
        return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # use p1, p2 as two diagnal point, see if p3, p4 is other two.
        points = [p1, p2, p3, p4]
        dists = defaultdict(int)
        for i, node1 in enumerate(points):
            for j in xrange(i + 1, 4):
                currDist = self.calcDist(node1, points[j])
                dists[currDist] += 1

        if 0 in dists:
            return False
        else:
            return len(dists.values()) == 2 and 2 in dists.values() and 4 in dists.values()