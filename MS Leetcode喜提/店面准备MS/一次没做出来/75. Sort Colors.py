class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white = 0, 0
        for i in xrange(len(nums)):
            val = nums[i]
            if val == 2:
                continue
            elif val == 1:
                nums[i] = 2
                nums[white] = 1
                white += 1
            else:
                nums[i] = 2
                nums[white] = 1
                nums[red] = 0
                white += 1
                red += 1