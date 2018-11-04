# coding=utf-8

# 注意向内缩的时候要 end - i + start

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        start, end = 0, len(matrix) - 1
        while start < end:
            for i in xrange(start, end):
                matrix[start][i], matrix[i][end] = matrix[i][end], matrix[start][i]
                matrix[start][i], matrix[end][end - i + start] = matrix[end][end - i + start], matrix[start][i]
                matrix[start][i], matrix[end - i + start][start] = matrix[end - i + start][start], matrix[start][i]
            start += 1
            end -= 1
            #print matrix