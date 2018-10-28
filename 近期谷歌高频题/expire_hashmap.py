from collections import defaultdict
class hashMap(object):
    def __init__(self):
        self.dicts = defaultdict(tuple)

    def getCurrtime(self):
        return 1

    def put(self, key, value, duration):
        experiation_time = duration + self.getCurrtime()
        self.dicts[key] = (value, experiation_time)


    def get(self, key):
        if key not in self.dicts: return None
        if self.dicts[key][1] < self.getCurrtime():
            del self.dicts[key]
            return None
        return self.dicts[key][0]
