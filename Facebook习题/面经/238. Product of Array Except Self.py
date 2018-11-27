class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num0s = nums.count(0)
        if num0s >= 2:
            return [0] * len(nums)
        if num0s == 1:
            index0 = nums.index(0)
            tmp = 1
            for i in xrange(len(nums)):
                if i == index0: continue
                tmp *= nums[i]
            res = [0] * len(nums)
            res[index0] = tmp
            return res

        res = [1] * len(nums)
        # build the left
        for i in xrange(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        prev = 1
        for i in xrange(len(nums) - 2, -1, -1):
            prev *= nums[i + 1]
            res[i] *= prev

        return res