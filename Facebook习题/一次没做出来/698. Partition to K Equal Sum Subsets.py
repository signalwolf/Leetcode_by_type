# coding=utf-8

class Solution(object):

    def helper(self, nums, index, GroupSums, target):
        if index == len(nums):
            return True

        for i, sums in enumerate(GroupSums):
            if nums[index] + sums > target:
                continue
            else:
                # 特别注意这里：
                # if GroupSums[i] + nums[index] == target or (index != len(nums)  - 1 and sums + nums[index] + nums[-1] <= target):
                GroupSums[i] += nums[index]
                if self.helper(nums, index + 1, GroupSums, target):
                    return True
                GroupSums[i] -= nums[index]
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = sum(nums)
        if sums % k != 0: return False
        target = sums / k
        nums.sort(reverse=True)
        return self.helper(nums, 0, [0] * k, target)

