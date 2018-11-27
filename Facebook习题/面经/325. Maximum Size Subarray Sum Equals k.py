class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = 0
        dicts = {0: -1}
        res = 0
        for i in xrange(len(nums)):
            sums += nums[i]
            if sums - k in dicts:
                res = max(res, i - dicts[sums - k])

            if sums not in dicts:
                dicts[sums] = i

        return res