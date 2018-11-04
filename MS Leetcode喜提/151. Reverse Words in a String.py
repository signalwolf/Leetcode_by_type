class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        start, lens, end = 0, len(s), 0

        while end < lens:
            while start < lens and s[start] == ' ':
                start += 1

            end = start
            while end < lens and s[end] != ' ':
                end += 1
            if end != start:
                stack.append(s[start: end])
            start = end

        return ' '.join(stack[::-1])