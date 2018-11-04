class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # if n == 1: return 'A'
        res = ''
        # n = n -1
        base = ord('A')
        while n != 0:
            res += chr(base + (n - 1) % 26)
            n = (n - 1)/26
        return res[::-1]