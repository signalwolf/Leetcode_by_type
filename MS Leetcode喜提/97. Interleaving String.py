
# 28ms
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len3 != len1 + len2: return False

        dp = [[False for _ in xrange(len2 + 1)] for _ in xrange(len1 + 1)]
        dp[0][0] = True

        for i in xrange(1, len1 + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break

        for j in xrange(1, len2 + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break

        for i in xrange(1, len1 + 1):
            for j in xrange(1, len2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (
                            dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])

        # print dp
        return dp[len1][len2]