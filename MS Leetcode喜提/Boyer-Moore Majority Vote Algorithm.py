
# Leetcode: 229. Majority Element II

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # required O(n) and O(1) space
        candidate0, candidate1 = 0, 1
        count0, count1 = 0, 0
        for num in nums:

            if num == candidate0:
                count0 += 1
            elif num == candidate1:
                count1 += 1

            elif count0 == 0:
                candidate0, count0 = num, 1
            elif count1 == 0:
                candidate1, count1 = num, 1


            else:
                count0 -= 1
                count1 -= 1
        res = []
        for i in (candidate0, candidate1):
            if nums.count(i) > len(nums) / 3:
                res.append(i)
        return res


