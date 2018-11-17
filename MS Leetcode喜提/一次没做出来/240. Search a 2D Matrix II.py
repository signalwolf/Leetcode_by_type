class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        M, N = len(matrix), len(matrix[0])
        row, col = M - 1, 0
        while row >= 0 and col < N:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False