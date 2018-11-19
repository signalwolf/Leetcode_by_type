class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        if len(needle) > len(haystack): return -1
        # if needle == haystack: return 0

        # dicts = collections.defaultdict(int)
        lens = len(needle)
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i:i + lens] == needle:
                return i
        else:
            return -1