class Solution(object):

    def distanceCalc(self, s):
        stack = []
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        currLevel = set()
        currLevel.add(s)
        distance = self.distanceCalc(s)
        while distance:
            nextLevel = set()
            while currLevel:
                s = currLevel.pop()
                c1, c2 = s.count('('), s.count(')')

                # interesting found: if c1 == c2, remove '(' or ')' doesn't matter:
                # enhanced from 76ms to 56ms, 30% enhance
                if c1 > c2:
                    target = ['(']
                elif c1 < c2:
                    target = [')']
                else:
                    target = ['(', ')']

                for i in xrange(len(s)):
                    if s[i] in target:
                        newS = s[:i] + s[i + 1:]
                        # at here, validate the newS in nextLevel or not before distance cal can speed up the check a lot
                        # 128ms --> 76ms == 40% enhance
                        if newS not in nextLevel and self.distanceCalc(newS) == distance - 1:
                            nextLevel.add(newS)
            currLevel = nextLevel
            distance -= 1

        return list(currLevel)