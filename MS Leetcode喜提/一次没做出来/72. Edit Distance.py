class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M, N = len(word1), len(word2)

        # initial:
        dp = [[0 for _ in xrange(N + 1)] for _ in xrange(M + 1)]
        for i in xrange(1, M + 1):
            dp[i][0] = i

        for j in xrange(1, N + 1):
            dp[0][j] = j

        # change
        for i in xrange(1, M + 1):
            for j in xrange(1, N + 1):
                thrid_element = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    thrid_element += 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, thrid_element)
        # print dp
        return dp[M][N]