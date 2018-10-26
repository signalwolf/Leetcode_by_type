# coding=utf-8
# 记得从后往前找，然后sort的使用，注意posision 可能没有sort
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        res = len(position)
        if res == 0:
            return 0
        combined = zip(position, speed)
        combined.sort(key=lambda x: x[0])
        # time = [0] * len(combined)
        # for i in xrange(len(combined)):
        time = [(target - combined[i][0]) / float(combined[i][1]) for i in xrange(len(combined))]

        last_time = time[-1]
        for i in xrange(len(position) - 2, -1, -1):
            curr_time = time[i]
            if curr_time <= last_time:
                res -= 1
            else:
                last_time = curr_time
        return res