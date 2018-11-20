
from collections import deque
class limitedSizeQueue(object):
    def __init__(self, size):
        self.size = size
        self.queue = deque([])

    def insert(self, val):
        if len(self.queue) == self.size:
            self.queue.popleft()

        self.queue.append(val)

    def remove(self):
        self.queue.popleft()

    # def list(self):
    #
    # def counter(self):
