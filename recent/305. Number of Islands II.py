# run out of time

from collections import defaultdict
class Solution(object):

    def helper(self, island, merge):
        merged, merged_set = merge[0], island[merge[0]]
        for i in xrange(1, len(merge)):
            merged_set = merged_set.union(island[merge[i]])
            del island[merge[i]]
        island[merged] = merged_set

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        island = defaultdict(set)
        num = 0
        ans = []
        visited = set()
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i, j in positions:
            if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                merge = []
                for key in island.keys():
                    for dx, dy in move:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and (x, y) in island[key]:
                            merge.append(key)
                if len(merge) >= 2:
                    island[merge[0]].add((i, j))
                    self.helper(island, merge)
                if len(merge) == 1:
                    island[merge[0]].add((i, j))
                if len(merge) == 0:
                    island[num].add((i, j))
                    num += 1
            ans.append(len(island))
        return ans
