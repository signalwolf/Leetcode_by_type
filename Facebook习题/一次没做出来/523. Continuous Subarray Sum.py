class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return sum(nums) == 0 and len(nums) > 1
        k = abs(k)
        dicts = {0:-1}
        sums = 0
        for i in xrange(len(nums)):
            sums += nums[i]
            sums %= k
            if sums not in dicts:
                dicts[sums] = i
            else:
                if i - dicts[sums] > 1:
                    return True
        else:
            return False