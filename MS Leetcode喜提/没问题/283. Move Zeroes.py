class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, zero_size = 0, 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                if zero_size == 0:
                    zero, zero_size = i, 1
                else:
                    zero_size += 1
            else:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1