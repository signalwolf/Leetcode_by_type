# under equal key scenario, the min heap will sort base on second key

from heapq import heappush, heappop
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap = []
        count = Counter(words)
        for word, freq in count.items():
            heappush(heap, (-freq, word))
        res = []
        for i in xrange(k):
            res.append(heappop(heap)[1])
        return res