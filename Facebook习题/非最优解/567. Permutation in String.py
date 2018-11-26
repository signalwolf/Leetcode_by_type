# coding=utf-8

# 关键在于思考permutation的本质就是其中的char的数量相同。

class Solution(object):

    def counter(self, s):
        base = ord('a')
        res = [0] * 26
        for char in s:
            res[ord(char) - base] += 1
        return res

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False
        count1 = self.counter(s1)
        count2 = self.counter(s2[:len1])
        # print count1, count2
        base = ord('a')
        if count2 == count1: return True

        for i in xrange(1, len2 - len1 + 1):
            # update count2 first:
            count2[ord(s2[i - 1]) - base] -= 1
            count2[ord(s2[i + len1 - 1]) - base] += 1

            if count2 == count1:
                return True
        return False