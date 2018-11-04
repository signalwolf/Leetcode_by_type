class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def helper(res, start, n):
            if n == 0: return
            if n == 1:
                res[start][start] = res[start][start - 1] + 1
                return

            for i in xrange(0, n):
                res[start][i + start] = res[start][i + start - 1] + 1
            for i in xrange(1, n):
                res[i + start][n - 1 + start] = res[i - 1 + start][n - 1 + start] + 1
            for i in xrange(1, n):
                res[n - 1 + start][n - 1 - i + start] = res[n - 1 + start][n - i + start] + 1
            for i in xrange(1, n - 1):
                res[n - 1 - i + start][start] = res[n - i + start][start] + 1

            # print res, n
            helper(res, start + 1, n - 2)

        res = [[0 for _ in xrange(n)] for _ in xrange(n)]
        helper(res, 0, n)
        return res