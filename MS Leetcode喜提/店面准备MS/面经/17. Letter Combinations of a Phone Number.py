# coding=utf-8

# 注意的是对empty string以及按到了非数字及1的处理

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = ['']
        for num in digits:
            next_res = []
            if num.isdigit() and int(num) != '1':
                potential = mapping[int(num)]
                for p in potential:
                    for s in res:
                        next_res.append(s + p)
            else:
                return False
            res = next_res
        return res