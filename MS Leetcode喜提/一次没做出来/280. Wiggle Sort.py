# coding=utf-8

# 这个题目需要注意的事情就是不停的换是可以解决问题的。

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        larger = True
        for i in xrange(0, len(nums) - 1):
            if larger:
                if nums[i] >= nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] <= nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            larger = not larger