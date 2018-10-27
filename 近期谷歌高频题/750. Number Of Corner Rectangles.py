


# only hit 6.14%
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def counter(x, y):
            count = 0
            for i in xrange(len(grid[0])):
                if grid[x][i] == grid[y][i] == 1:
                    count += 1
            if count <= 1: return 0
            return count * (count - 1) / 2

        if len(grid) == 0 or len(grid[0]) == 0: return 0
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(i + 1, len(grid)):
                res += counter(i, j)
        return res