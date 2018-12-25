class Solution(object):

    def dfs(self, point, board, word, index, visited):
        if index == len(word):
            return True

        visited.add(point)
        x, y = point
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) \
                    and (nx, ny) not in visited and board[nx][ny] == word[
                index]:
                if self.dfs((nx, ny), board, word, index + 1, visited):
                    return True

        # remember to step back by remove the point from visited:
        visited.remove(point)
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return False
        if not board or not board[0]: return False
        m, n = len(board), len(board[0])
        initial = []
        chars = collections.Counter(list(word))

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    initial.append((i, j))
                if board[i][j] in chars:
                    chars[board[i][j]] -= 1
                    if chars[board[i][j]] == 0:
                        del chars[board[i][j]]

        if chars:
            return False

        # print initial

        for startpoint in initial:
            if self.dfs(startpoint, board, word, 1, set()):
                return True
        return False
