from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        currSum = 0
        count[0] = 1
        res = 0
        for i in xrange(len(nums)):
            currSum += nums[i]
            if currSum - k in count:
                res += count[currSum - k]
            count[currSum] += 1
        return res