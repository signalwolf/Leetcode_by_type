from heapq import heappush, heappop
from random import randint
class hashmap(object):

    def __init__(self):
        self.hash = {}
        self.heap = []


    def get(self, key, time):
        value, expire_time = self.hash[key]
        self.clean(time)
        if key in self.hash:
            return self.hash[key]
        else:
            return None

    def clean(self, time):
        while len(self.heap) > 0 and self.heap[0][0] < time:
            _, key = heappop(self.heap)
            del self.hash[key]

    def set(self, key, value, expire):
        self.hash[key] = (value, expire)
        heappush(self.heap, (expire, key))


hash = hashmap()
for i in xrange(10):
    curr_time = randint(0, 10)
    hash.set(i, i, curr_time)
print hash.hash
hash.clean(20)
print hash.hash

