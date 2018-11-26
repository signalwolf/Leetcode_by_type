# coding=utf-8

# 关键在于思考permutation的本质就是其中的char的数量相同。

class Solution(object):

    def diff(self, A, B):
        res = 0
        for i in xrange(26):
            if A[i] <= B[i]:
                continue
            else:
                res += A[i] - B[i]

        return res

    def counter(self, s):
        base = ord('a')
        res = [0] * 26
        for char in s:
            res[ord(char) - base] += 1
        return res

    def checkInclusion(self, s1, s2, k):
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
        if self.diff(count2, count1) <= k:
            return s2[:len1]

        for i in xrange(1, len2 - len1 + 1):
            # update count2 first:
            count2[ord(s2[i - 1]) - base] -= 1
            count2[ord(s2[i + len1 - 1]) - base] += 1

            if self.diff(count2, count1) <= k:
                return s2[i:i + len1]
        return False



tmp = Solution()
print tmp.checkInclusion("algorithm", "altruistic", 4)
c1, c2 = tmp.counter("algorithm"), tmp.counter("altruisti")
print tmp.diff(c1,c2)