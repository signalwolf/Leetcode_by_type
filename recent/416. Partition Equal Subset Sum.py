class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        sums /= 2
        nums.sort(reverse=True)
        if nums[0] > sums:
            return False

        def backtrack(start, target):
            if target < 0:
                return False
            if target == 0:
                return True
            for i in range(start, len(nums)):
                if backtrack(i + 1, target - nums[i]):
                    return True
            return False

        return backtrack(0, sums)


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        sums /= 2
        nums.sort(reverse=True)
        if nums[0] > sums:
            return False

        dp = [False] * (sums + 1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(sums, 0, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[sums]


