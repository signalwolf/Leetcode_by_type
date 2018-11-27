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

# rewrite:
class Solution(object):

    def backtracking(self, nums, index, target, sums):
        if index == len(nums):
            return True

        # print sums, target
        for j, currSum in enumerate(sums):
            if currSum + nums[index] != target and currSum + nums[index] + nums[-1] > target:
                continue
            sums[j] = currSum + nums[index]
            if self.backtracking(nums, index + 1, target, sums):
                return True
            sums[j] = currSum
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0 or len(nums) == 0: return False
        nums.sort(reverse=True)
        return self.backtracking(nums, 0, total / k, [0] * k)

