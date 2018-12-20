from random import randint
import time

def findtarget(A, B, target):
    res = []
    diff = float('inf')
    for indA, valA in enumerate(A):
        for indB, valB in enumerate(B):
            if valA + valB <= target:
                currDiff = target - valA - valB
                if currDiff < diff:
                    diff = currDiff
                    res = [[indA, indB]]
                elif currDiff == diff:
                    res.append([indA, indB])
    return res

from collections import defaultdict
from bisect import bisect_left
def indmap(A):
    dicts = defaultdict(list)
    for index, value in enumerate(A):
        dicts[value].append(index)
    return dicts


def optimized(A, B, target):
    Aind, Bind = indmap(A), indmap(B)

    sortedB = sorted(B)

    smallest, biggest = sortedB[0], sortedB[-1]
    res = []
    diff = float('inf')
    for val in A:
        if val + smallest > target:
            continue
        if val + biggest < target:
            currDiff = target - val - biggest
            index = len(sortedB)
        else:
            # val + smallest <= target, val + biggest >= target:
            index = bisect_left(sortedB, target - val)

            if sortedB[index] + val == target:
                currDiff = 0
                index += 1
            else:
                currDiff = target - val - sortedB[index - 1]

        if currDiff < diff:
            res = [[val, sortedB[index - 1]]]
            diff = currDiff
        elif currDiff == diff:
            res.append([val, sortedB[index - 1]])

    # print currDiff
    # print sorted(set(map(tuple, res)))


    ans = []

    for valA, valB in set(map(tuple, res)):
        indA = Aind[valA]
        indB = Bind[valB]
        for i in indA:
            for j in indB:
                ans.append((i, j))
    return ans



A = [randint(0, 100) for _ in xrange(100)]
B = [randint(0, 100) for _ in xrange(100)]
print A, B
start = time.clock()
# solution#1:
# O(m log m + n log n + n log m ) = O (m + n) * log m + n * log n)
res = findtarget(A, B, 20)
print (time.clock() - start)
tmp = set()
print sorted(res)
for indA, indB in res:
    tmp.add( (A[indA], B[indB]))
# print sorted(tmp)

print len(set(map(tuple, res))) == len(res)
# print sorted(set(map(tuple, res)))

start = time.clock()
# solution#2:
res =  optimized(A, B, 20)
print (time.clock() - start)
print sorted(res)