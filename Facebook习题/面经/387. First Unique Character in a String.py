class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # you must iterate s to remember the count
        count = [0] * 26
        base = ord('a')
        s = list(s)
        # do the counting
        for i, char in enumerate(s):
            s[i] = ord(char) - base
            count[s[i]] += 1
        # find the first count == 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1