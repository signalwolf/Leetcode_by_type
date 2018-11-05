# coding=utf-8

# 很多的conner case 没有想到，尤其是 '+' '-' 的情况

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str: return 0
        max_int, min_int = 2 ** 31 - 1, - 2 ** 31
        res, found = [], False
        for s in str:
            if not found:
                if s == '+' or s == '-' or s.isdigit():
                    if s != '+':
                        res.append(s)
                    found = not found
                elif s != ' ':
                    return 0
            else:
                if s.isdigit():
                    res.append(s)
                else:
                    break
        res = ''.join(res)
        if res == '-' or not res: return 0
        res = int(res)
        if res >= max_int: return max_int
        if res <= min_int: return min_int
        return res