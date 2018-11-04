# there is an better solution

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.player = {1: set(), 2: set()}
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

        def check_winer():
            # res = False
            for i in xrange(self.n):
                if (row, i) not in curr_player_moves:
                    break
            else:
                return True

            for i in xrange(self.n):
                if (i, col) not in curr_player_moves:
                    break
            else:
                return True

            if row == col:
                for i in xrange(self.n):
                    if (i, i) not in curr_player_moves:
                        break
                else:
                    return True

            if row == self.n - col - 1:
                for i in xrange(self.n):
                    if (i, self.n - i - 1) not in curr_player_moves:
                        break
                else:
                    return True

            return False

        curr_player_moves = self.player[player]
        curr_player_moves.add((row, col))
        ans = check_winer()
        # print self.player
        if ans:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)