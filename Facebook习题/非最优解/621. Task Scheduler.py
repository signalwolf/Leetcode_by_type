# coding=utf-8

# 最优解：
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_count = Counter(tasks).values()
        max_count = max(tasks_count)
        task_amount = tasks_count.count(max_count)
        return max(len(tasks), (n+1)*(max_count-1)+task_amount)


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        res = 0
        countDict = Counter(tasks)
        count = sorted(countDict.values())

        while count:
            # res should be extend to n + 1
            prev = len(count)
            res += n + 1
            tmp = n + 1
            # keep remove n element from the count, if count = 0, pop out it:
            for i in xrange(len(count) - 1, -1, -1):
                count[i] -= 1
                if count[i] == 0:
                    count.pop(i)
                tmp -= 1
                if tmp == 0:
                    break
            count.sort()
        return res - (n + 1 - prev)