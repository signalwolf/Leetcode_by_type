class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: return
        N = len(matrix)
        start, end = 0, N - 1
        while start < end:
            for i in xrange(start, end):
                matrix[start][i], matrix[start + i - start][end] = matrix[start + i - start][end], matrix[start][i]

            for i in xrange(start, end):
                matrix[start][i], matrix[end][end - i + start] = matrix[end][end - i + start], matrix[start][i]

            for i in xrange(start, end):
                matrix[start][i], matrix[end - i + start][start] = matrix[end - i + start][start], matrix[start][i]

            start += 1
            end -= 1
        return 