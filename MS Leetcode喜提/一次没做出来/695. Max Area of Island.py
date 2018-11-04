class Solution(object):
    area = 0

def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def dfs(i, j):
        if grid[i][j] == 1:
            self.area += 1
            grid[i][j] = 2

        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            x, y = i + dx, j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                dfs(x, y)

    maxarea = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == 1:
                self.area = 0
                dfs(i, j)
                maxarea = max(maxarea, self.area)
    return maxarea