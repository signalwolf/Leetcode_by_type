# coding=utf-8

# 关键在于如果有5和2，那么就一定有10。而2是非常多的，远比5多，因此可以只考虑5
# n! 中5 的个数是什么呢？
# 5, 10, 15, 20, 25, 30, 35 ...
# 1,  1,  1,  1,  2,  1,  1



class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if it have 5 and 2, then one trailing zeros
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)