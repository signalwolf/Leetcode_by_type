class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # backward move the curser:
        p1, p2, pt = m - 1, n - 1, len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            # print nums1, p1, p2
            if nums1[p1] > nums2[p2]:
                nums1[pt] = nums1[p1]
                p1 -= 1
            else:
                nums1[pt] = nums2[p2]
                p2 -= 1
            pt -= 1

        if p1 < 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]

        return