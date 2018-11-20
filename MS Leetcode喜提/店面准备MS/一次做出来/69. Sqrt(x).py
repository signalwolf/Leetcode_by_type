class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: return x
        start, end = 1, x
        while start + 1< end:
            mid = start + (end - start) / 2
            if mid ** 2 > x:
                end = mid
            elif mid ** 2 < x:
                start = mid
            else:
                return mid
        return start