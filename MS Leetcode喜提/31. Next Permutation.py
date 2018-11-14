class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums) - 1, 0, - 1):
            if nums[i - 1] < nums[i]:
                nums[i:] = nums[i:][::-1]
                for j in xrange(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        return
        return nums.reverse()