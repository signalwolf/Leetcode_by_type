class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = ''
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(int(num))
                stack.append('[')
                num = ''
            elif char == ']':
                inner = ''
                while stack[-1] != '[':
                    inner = stack.pop() + inner
                stack.pop()
                inner = stack.pop() * inner
                stack.append(inner)
            else:
                stack.append(char)
        res = ''
        for string in stack:
            res += string
        return res