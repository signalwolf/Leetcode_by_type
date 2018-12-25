# coding=utf-8
# 三层 dp, 第一层找到KSums; 第二层找到twoNums, 第三层找到threeNums:

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        KSum = [0] * (len(nums) - k + 1)
        KSum[0] = sum(nums[:k])
        # step1: build up KSum: O(n)
        for i in xrange(1, len(KSum)):
            KSum[i] = KSum[i - 1] - nums[i - 1] + nums[i + k - 1]

        # step2: build up twoNums:
        # format: maxSum, index
        maxSum, index = 0, 2
        twoNums = [[0 for _ in xrange(3)] for _ in xrange(len(KSum) - k)]

        twoNums[len(KSum) - 1 - k][maxSum] = KSum[len(KSum) - 1]
        twoNums[len(KSum) - 1 - k][1] = len(KSum) - 1 - k
        twoNums[len(KSum) - 1 - k][index] = len(KSum) - 1

        for i in xrange(len(twoNums) - 2, k - 1, -1):
            if twoNums[i + 1][maxSum] > KSum[i + k]:
                twoNums[i] = twoNums[i + 1][:]
            else:
                twoNums[i] = [KSum[i + k], 0, i + k]
            twoNums[i][1] = i

        # step3: build up threeNums:
        threeNums = [[0 for _ in xrange(4)] for _ in xrange(len(twoNums) - k)]
        threeNums[len(twoNums) - 1 - k][maxSum] = twoNums[len(twoNums) - 1][maxSum] + KSum[len(twoNums) - 1]
        threeNums[len(twoNums) - 1 - k][1] = len(twoNums) - 1 - k
        threeNums[len(twoNums) - 1 - k][2] = twoNums[len(twoNums) - 1][1]
        threeNums[len(twoNums) - 1 - k][3] = twoNums[len(twoNums) - 1][2]

        currMaxsum = threeNums[len(twoNums) - 1 - k][maxSum] + KSum[len(twoNums) - 1 - k]
        res = threeNums[len(twoNums) - 1 - k][1:]

        for i in xrange(len(threeNums) - 2, -1, -1):
            if threeNums[i + 1][maxSum] > twoNums[i + k][maxSum] + KSum[i + k]:
                threeNums[i] = threeNums[i + 1][:]
                threeNums[i][1] = i
            else:
                threeNums[i] = [twoNums[i + k][maxSum] + KSum[i + k], i, twoNums[i + k][1], twoNums[i + k][2]]

            if threeNums[i][maxSum] + KSum[i] >= currMaxsum:
                currMaxsum = threeNums[i][maxSum] + KSum[i]
                res = threeNums[i][1:]
        return res