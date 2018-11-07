# coding=utf-8

# 我的想法是
#   我随机选一个人，然后看这个人是否know anyone in potential group
#   如果他知道其中任何一个人，那么他就不可能是要找的那个人，
#

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
from random import randint
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = randint(0, n - 1)
        for i in xrange(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in xrange(x)):
            return -1
        if any(not knows(i, x) for i in xrange(n)):
            return -1
        return x