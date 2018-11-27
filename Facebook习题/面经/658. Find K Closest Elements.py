# coding=utf-8
# 最简单的办法，用heap来遍历，最后保留 K 个，时间复杂度是 O(nlogk)
# 使用two pointer 的办法：O(2logn) 用于找 left, right; 然后移动left，right, K步就好 --》 O(k)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        index_left = bisect.bisect_left(arr, x)
        index_right = bisect.bisect_right(arr, x)
        # print index_left, index_right
        # res = []
        n = index_right - index_left

        if n >= k:
            return [x] * k
        else:
            k -= n

        left, right = index_left - 1, index_right

        while k:

            disleft = abs(x - arr[left]) if left >= 0 else float('inf')
            disright = abs(x - arr[right]) if right < len(arr) else float('inf')

            if disleft <= disright:
                k -= 1
                left -= 1
            else:
                k -= 1
                right += 1

        return arr[left + 1:right]
