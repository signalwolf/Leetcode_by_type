# coding=utf-8

# 注意的细节就是在最后只有单列或者只有单行或者只有一个的时候要特殊处理。
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        res = []
        start, rowEnd, colEnd = 0, len(matrix) - 1, len(matrix[0]) - 1
        while start <= rowEnd and start <= colEnd:
            if start == rowEnd == colEnd:
                res.append(matrix[start][start])
            elif start == rowEnd:
                for i in xrange(start, colEnd + 1):
                    res.append(matrix[start][i])
            elif start == colEnd:
                for i in xrange(start, rowEnd + 1):
                    res.append(matrix[i][start])
            else:
                for i in xrange(start, colEnd):
                    res.append(matrix[start][i])

                for i in xrange(start, rowEnd):
                    res.append(matrix[i][colEnd])

                for i in xrange(start, colEnd):
                    res.append(matrix[rowEnd][colEnd - i + start])

                for i in xrange(start, rowEnd):
                    res.append(matrix[rowEnd - i + start][start])

            start += 1
            rowEnd -= 1
            colEnd -= 1

        return res