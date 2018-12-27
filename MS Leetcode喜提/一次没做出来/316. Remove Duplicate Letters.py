# coding=utf-8
# 使用贪心法来解决问题，通过stack来计算

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        position = [0 for _ in xrange(26)]
        base = ord('a')
        # 记录下当前char的最后一个位置，在之后，用于判断在某点之后是否还有同样的char
        for i, char in enumerate(s):
            position[ord(char) - base] = i

        # stack 使用的是贪心算法，每个时刻stack中的元素都是最优解
        stack = []
        # seen 用于确保stack不存在重复项:
        seen = set()

        for i, char in enumerate(s):
            # 如果当前的char 看过，那么对于最优解来说，修改一个已经存在的char是无意义的：
            # 1. char 在stack的末尾，那么修改无意义
            # 2. char 不在stack的末尾，那么根据 stack的定义，最优解被打破了
            if char not in seen:
                # 如果stack的最后项比char大并且这个最后项能被后放，那么remove掉，之后再加
                # 否则就直接加到末尾
                while stack and stack[-1] > char and position[ord(stack[-1]) - base] > i:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                seen.add(char)
        return ''.join(stack)