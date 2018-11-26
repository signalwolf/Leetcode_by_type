# coding=utf-8

# "
# 1 给一个positive array，和一个target， 是否存在一个连续的 subarray 之和为 target？ 返回 true or false。 类似two sum。
#
# 口头说了暴力 n^2 解， hashSet 解以及双指针解。最后写了双指针解。 写完有一个小bug，小哥指出后迅速改正。"

# Brute force: check all combination: O(n**2)
# Hashset: remember the currSum, if currSum - target in dicts: return True; After for loop, return False

# both solution overkill the problem, the key here is positive. So, in another word, the sum is keep increasing.
# two pointer:
# p1, p2 = start, start
# sums(p1, p2) < target: increase p2, sums += nums[p2]
# sums(p1, p2) > target: increase p1, sums -= nums[p1]

def solution1(nums, target):

    # j not included
    i, j, currSum = 0, 0, 0

    while i < len(nums):

        # move j forward till j == len(nums) or sums(i, j) >= target
        while j < len(nums)  and currSum < target:
            currSum += nums[j]
            j += 1

        # condition#1: sums(nums[i:j]) == target:
        if currSum == target: return i, j

        # condition#2: sums(nums[i:j]) > target:
        # move i till i == j or sums(i, j) <= target
        while i < j and currSum > target:
            currSum -= nums[i]
            i += 1

        # sub condition #1: sum == target
        if currSum == target:
            return i, j
        # sub-condition #2: sum < target:
        else:
            i = j

    return False

from collections import defaultdict
def solution2 (nums, target):
    count = defaultdict(list)
    count[0] = [-1]
    currSum = 0
    for i in xrange(len(nums)):
        currSum += nums[i]
        if currSum - target in count:
            return i, count[currSum - target], count
        count[currSum].append(i)
    return False

print solution1([13, 12, 7, 2 , 15], 9)
print solution2([13, 12, 7, 2 , 15], 9)

