class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S, stack_T = [], []
        for char in S:
            if char != '#':
                stack_S.append(char)
            elif stack_S:
                stack_S.pop()

        for char in T:
            if char != '#':
                stack_T.append(char)
            elif stack_T:
                stack_T.pop()
        return stack_S == stack_T