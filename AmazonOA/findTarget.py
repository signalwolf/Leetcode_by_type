from random import randint

from bisect import bisect_left
def findtarget(listA, listB, target):
    # brute force (upper boundary): try each combination: m * n and find the result
    # sortA, sortB: mlogm + nlogn, binary search num from A in B. mlogn
    # total: mlogm + nlogn + mlogn
    listA.sort()
    listB.sort()
    # distance
    res = [float('inf'), None, None]
    smallest, biggest = listB[0], listB[-1]
    for val in listA:
        # currVal + biggest number in B not able to bigger than target, the maxSum = currVal + biggest
        if val + biggest < target:
            curr = val + biggest
            if target - curr < res[0]:
                res = [target - curr, val, biggest]
            continue

        # currVal + smallest number in B exceed target: we shall stop here
        if val + smallest > target:
            break

        # currVal + biggest > target and currVal + smallest < target
        index = bisect_left(listB, target - val)
        print index, val, listA, listB
        if target - val == listB[index]:
            return [val, listB[index]]
        else:
            curr = val + listB[index - 1]
            if target - curr < res[0]:
                res = [target - curr, val, listB[index - 1]]
    return res[1:]

A = [randint(0, 100) for _ in xrange(10)]
B = [randint(0, 100) for _ in xrange(10)]
print A, B
print findtarget(A, B, 100)


