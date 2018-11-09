
# DP solution:50.67 %

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # case1: s is empty, if p is all *, then True, else False
        if len(s) == 0: return p == '*' * len(p)
        # case2: s is not empty and p is empty, False
        if len(p) == 0: return False

        M, N = len(s), len(p)

        # initial, consider len == 0 cases
        dp = [[False for _ in xrange(N + 1)] for _ in xrange(M + 1)]
        dp[0][0] = True

        for j in xrange(1, N + 1):
            if dp[0][j - 1] and p[j - 1] == "*":
                dp[0][j] = True
            else:
                break
        # change
        for i in xrange(1, M + 1):
            for j in xrange(1, N + 1):
                if p[j - 1] != '*':
                    dp[i][j] = True if (dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')) else False
                else:
                    dp[i][j] = True if (dp[i - 1][j] or dp[i][j - 1]) else False

        return dp[M][N]