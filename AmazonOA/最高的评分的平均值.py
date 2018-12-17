# coding=utf-8
# 第一题是给一个list，每个element是<productId, productRating>，求每个product最高的5个评分的平均值，
# 不是很难，不过要尽力快一点，第二题还是蛮花时间的。
from random import randint

from collections import defaultdict
from heapq import heappush, heappop

def findproductaverage(lists, k):
    res = defaultdict(list)
    for productID, rating in lists:
        print productID, rating
        heappush(res[productID], rating)
        if len(res[productID]) > k:
            heappop(res[productID])

    ans = []
    for key, value in res.items():
        ans.append([key, sum(value)/float(len(value))])
    return ans

productID = [randint(0, 10) for _ in xrange(30)]
rating = [randint(0, 5) for _ in xrange(30)]

lists = sorted(zip(productID, rating))

print findproductaverage(lists, 3)