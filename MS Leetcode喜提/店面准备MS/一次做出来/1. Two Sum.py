class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for i, num in enumerate(nums):
            if num in dicts:
                return [dicts[num], i]
            else:
                dicts[target - num] = i