class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        base = ord('A')
        for i in s:
            res = res * 26 + ord(i) - base + 1
        return res