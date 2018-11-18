# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        potential = set(range(n))
        while potential:
            nextP = set()
            currGuess = potential.pop()
            currGuessFlag = True
            for i in xrange(n):
                if i == currGuess: continue
                if knows(currGuess, i):
                    currGuessFlag = False
                    if i in potential:
                        nextP.add(i)
            potential = nextP

        if currGuessFlag:
            for i in xrange(n):
                if i == currGuess: continue
                if knows(i, currGuess):
                    continue
                else:
                    return -1
            else:
                return currGuess
        else:
            return -1