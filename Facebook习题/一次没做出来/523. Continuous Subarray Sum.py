# coding=utf-8

# 简化后的版本，更容易理解
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
        # get the sums
        for i in xrange(1, len(nums)):
            nums[i] = (nums[i] + nums[i - 1])

        dicts = {}
        dicts[0] = -1
        # 关键点在于说两个sum的%k 如果相同就代表 这两个中间的和为 n * k
        # sums[i] = nums[0] + nums[1] + nums[2] + ... + nums[i]
        # sums[j] = nums[0] + nums[1] + nums[2] + ... + nums[i] + nums[i + 1] + ... + nums[j]
        # sums[i:j] = sums[j] - sums[i] = nums[i + 1] + ... + nums[j]
        # if sums[i] = n1 * k + A and sums[j] = n2 * k + A:
        # then sums[i:j] = (n2 - n1) * k
        for i in xrange(len(nums)):
            curr = nums[i] % k
            if curr in dicts:
                if i - dicts[curr] > 1:
                    return True
            else:
                dicts[curr] = i
        return False

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

