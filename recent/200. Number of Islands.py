class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(i, j):
            grid[i][j] = 2
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x, y = i + dx, j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                    dfs(x, y)

        if not len(grid) or not len(grid[0]): return 0
        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        # print grid
        return count