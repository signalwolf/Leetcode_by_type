class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        def update_remain(num, start, k, index):
            if len(num) == k + start:
                remain[index:] = num[start:]
                return
            if k == 0:
                return

            min_val, min_ind = 10, len(num)
            for i in xrange(start, len(num) - k + 1):
                if num[i] < min_val:
                    min_val, min_ind = num[i], i

            remain[index] = min_val
            update_remain(num, min_ind + 1, k - 1, index + 1)

        num = map(int, list(num))
        k = len(num) - k
        if k == 0:
            return '0'
        remain = [0] * k
        update_remain(num, 0, k, 0)
        return str(int(''.join(map(str, remain))))