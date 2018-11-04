class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        if len(s) == 0: return 0
        ans = 0
        for i in xrange(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        else:
            ans += roman[s[-1]]
        return ans