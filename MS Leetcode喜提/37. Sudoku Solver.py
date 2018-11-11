class Solution(object):

    def validation(self, board, x, y):
        base = board[x][y]
        for i in xrange(9):
            if i == x: continue
            if board[i][y] == base:
                return False

        for j in xrange(9):
            if j == y: continue
            if board[x][j] == base:
                return False

        for i in xrange(x / 3 * 3, (x / 3 + 1) * 3):
            for j in xrange(y / 3 * 3, (y / 3 + 1) * 3):
                if i == x and j == y:
                    continue
                if board[i][j] == base:
                    return False
        return True

    def helper(self, board, x):
        for i in xrange(x, 9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for k in xrange(1, 10):
                        board[i][j] = str(k)
                        if self.validation(board, i, j) and self.helper(board, i):
                            return True
                    else:
                        board[i][j] = '.'
                        return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0)