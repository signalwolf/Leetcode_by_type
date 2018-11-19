# coding=utf-8

# 设计一个程序能够shuffle 52张扑克牌
# https://leetcode.com/problems/shuffle-an-array/description/

# Better solution: 使用互换的手段：

from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.original
        self.original = self.original[:]
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in xrange(len(self.nums)):
            index = randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums



# 我的方法：不好，因为每次pop都是O(n),故而每次的操作要 O(n2)
from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.original
        self.original = self.original[:]
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = []
        while self.nums:
            res.append(self.nums.pop(randint(0, len(self.nums) - 1)))
        self.nums = res
        return res
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()