# coding=utf-8

# 这个解决方案还是比较难的，如果真要按照答案写我估计写不出来
# 想法大概是这样的：
#   1.  由于要求说分成

# 特别注意最后出来要做count，并且不能用 if first, 因为first 可能 == 0

# k 分段的解决方法：
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = 2
        # format: value, count
        records = [[False, 0] for _ in xrange(k)]
        for num in nums:
            # print num, records
            for i, record in enumerate(records):
                if record[0] is False or record[0] == num:
                    record[0] = num
                    record[1] += 1
                    break
            else:
                for i in xrange(len(records) - 1, -1, - 1):
                    record = records[i]
                    if record[0] is not False:
                        record[1] -= 1
                        if record[1] == 0:
                            records.pop(i)
                            records.append([False, 0])
        res = []
        for record in records:
            # notice the is not False, this is critical
            if record[0] is not False and nums.count(record[0]) > len(nums) / (k + 1):
                res.append(record[0])
        return res


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first, second = False, False
        count = [0] * 2
        res = []
        for num in nums:
            # print first, second, count, num
            if first is False or num == first:
                first = num
                count[0] += 1
                continue
            if second is False or num == second:
                second = num
                count[1] += 1
                continue

            count[0] -= 1
            count[1] -= 1
            if count[0] == 0 and count[1] == 0:
                first = second = False
            elif count[1] == 0:
                second = False
            elif count[0] == 0:
                first = second
                count[0] = count[1]
                second = False
                count[1] = 0

        if first is not False and nums.count(first) > len(nums) / 3:
            res.append(first)
        if second is not False and nums.count(second) > len(nums) / 3:
            res.append(second)
        return res