# coding=utf-8

# 1. 最重要的是，每次update只要check那一行，那一列以及可能check两个diag的一个而不需要去check all
# 2. 其次就是不需要啊O(N**2)的space，我们只需要记住每行的sum，每列的sum就好
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rowSum = [0] * n
        self.colSum = [0] * n
        self.diag0 = self.diag1 = 0
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = self.n
        if 0 <= row < self.n and 0 <= col < self.n:
            # check row
            self.rowSum[row] = self.rowSum[row] + 1 if player == 1 else self.rowSum[row] - 1
            if self.rowSum[row] in [-n, n]:
                return player

            # check col:
            self.colSum[col] = self.colSum[col] + 1 if player == 1 else self.colSum[col] - 1
            if self.colSum[col] in [-n, n]:
                return player

            # check diag:
            if row == col:
                self.diag0 = self.diag0 + 1 if player == 1 else self.diag0 - 1
                if self.diag0 in [-n, n]:
                    return player

            if row == n - 1 - col:
                self.diag1 = self.diag1 + 1 if player == 1 else self.diag1 - 1
                if self.diag1 in [-n, n]:
                    return player

            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)