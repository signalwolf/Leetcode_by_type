from collections import defaultdict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict1 = defaultdict(list)
        self.dict2 = defaultdict(list)
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict1:
            val, count = self.dict1[key]
            self.dict2[count].remove(key)
            if not self.dict2[count]:
                del self.dict2[count]
            self.dict2[count + 1].append(key)
            self.dict1[key] = [val, count + 1]
            return val
        else:
            return -1

    def pop(self):
        smallest_count = min(self.dict2.keys())
        key = self.dict2[smallest_count].pop(0)
        if len(self.dict2[smallest_count]) == 0:
            del self.dict2[smallest_count]
        del self.dict1[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0: return None

        if key in self.dict1:
            val, count = self.dict1[key]
            self.dict2[count].remove(key)
            if not self.dict2[count]:
                del self.dict2[count]
            self.dict2[count + 1].append(key)
            self.dict1[key] = [value, count + 1]
        else:
            if len(self.dict1) == self.capacity:
                self.pop()
            self.dict1[key] = [value, 1]
            self.dict2[1].append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)