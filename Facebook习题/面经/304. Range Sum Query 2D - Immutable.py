class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.M, self.N = 0, -1
            return

        self.M, self.N = len(matrix), len(matrix[0])
        for i in xrange(1, self.M):
            matrix[i][0] += matrix[i - 1][0]
        for j in xrange(1, self.N):
            matrix[0][j] += matrix[0][j - 1]

        for i in xrange(1, self.M):
            for j in xrange(1, self.N):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] + matrix[i][j] - matrix[i - 1][j - 1]

        self.matrix = matrix
        # print matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > row2 or col1 > col2: return 0
        if row1 >= self.M or col1 >= self.N: return 0
        row1 = max(0, row1)
        col1 = max(0, col1)
        row2 = min(self.M - 1, row2)
        col2 = min(self.N - 1, col2)
        # equation:
        # matrix[row2][col2] - matrix[row1 - 1][col2] - matrix[row2][col1 - 1] + matrix[row1 - 1][col1 - 1]
        if row1 == col1 == 0:
            return self.matrix[row2][col2]
        if row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        if col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]

        return self.matrix[row2][col2] - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 - 1] + \
               self.matrix[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)