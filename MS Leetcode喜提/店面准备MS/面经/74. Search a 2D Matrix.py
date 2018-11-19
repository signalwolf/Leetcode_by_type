class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        M, N = len(matrix), len(matrix[0])
        start, end = 0, M * N - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            midRow, midCol = mid / N, mid % N
            if matrix[midRow][midCol] > target:
                end = mid
            elif matrix[midRow][midCol] < target:
                start = mid
            else:
                return True

        for index in [start, end]:
            row, col = index / N, index % N
            if matrix[row][col] == target:
                return True
        else:
            return False