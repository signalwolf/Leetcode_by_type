class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        memory = [0] * (n + 1)
        memory[0:4] = [1, 1, 2, 5]
        for i in xrange(4, n + 1):
            for left in xrange(0, i):
                right = i - left - 1
                memory[i] += memory[left] * memory[right]
        return memory[n]