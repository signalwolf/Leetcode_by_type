class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(i, j):
            mark[i][j] = 1
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x, y = i + dx, j + dy
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] >= matrix[i][j] and not mark[x][y]:
                    dfs(x, y)

        def dfs2(i, j):
            if mark[i][j] == 1:
                res.append([i, j])
                mark[i][j] = 2
            else:
                mark[i][j] = -1
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x, y = i + dx, j + dy
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] >= matrix[i][j] and mark[x][
                    y] not in (-1, 2):
                    dfs2(x, y)

        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        mark = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        res = []
        for i in xrange(len(matrix)):
            dfs(i, 0)

        for i in xrange(len(matrix[0])):
            dfs(0, i)

        for i in xrange(len(matrix)):
            dfs2(i, len(matrix[0]) - 1)

        for i in xrange(len(matrix[0])):
            dfs2(len(matrix) - 1, i)

        return res
