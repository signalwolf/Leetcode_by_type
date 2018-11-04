# coding=utf-8

# 这个算法有很多
# 1. Lomuto partition algorithm
# 算法比较难以理解，
# 首先两个point tracker来记录已经有了多少 red/white，而blue的pointer所指向的就是当前位置，因为
# 最后的一定是blue。
# 如果当前的是blue的话，那么什么都不做，因为当前的已经sorted了
# 如果当前的是white的话，那么我需要将它插入到white的pointer的位置：
    # white pointer 的位置有两种可能：
        # 它是blue，那么我将当前位置（blue 位）位改为2，white pointer 改为1就好
        # 它就是当前的位置，代表之前没有2，故而将当前位改为1就好。
# 如果当前的是red的话， 那么我需要将它插入到red的pointer的位置。
    # red pointer 的位置有三种可能：
        # 它是blue，那么将当前位置 （blue 位）改为2 就好，red位改为0
        # 它是就是当前位，代表之前全为 1， 故而将当前位置改为0就好
        # 它是white，那么就比较复杂了：
            # 第一步，将red位改为 0， 这样少了一个white，多了一个red。故而重复第二部将white位插入到数组中
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white = 0, 0
        for i in xrange(len(nums)):
            val = nums[i]
            nums[i] = 2
            if val < 2:
                nums[white] = 1
                white += 1
            if val == 0:
                nums[red] = 0
                red += 1

# 稍微易懂点的算法：
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

