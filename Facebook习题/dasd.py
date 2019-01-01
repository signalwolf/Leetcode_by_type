class LinkedListNode(object):
    def __init__(self, key, count):
        self.count = count
        self.key = [key]
        self.prev = None
        self.next = None


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}
        self.min = LinkedListNode('min', 0)
        self.max = LinkedListNode('max', 0)
        self.min.next = self.max
        self.max.prev = self.min

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.count:
            if self.min.next == self.max or self.min.next.count != 1:
                newNode = LinkedListNode(key, 1)
                newNode.prev = self.min
                newNode.next = self.min.next
                self.min.next.prev = newNode
                self.min.next = newNode
                self.count[key] = newNode
            else:
                self.min.next.key.append(key)
        else:
            currNode = self.count[key]
            # case1: need to add new node
            if currNode.next == self.max or currNode.next.count != currNode.count + 1:
                # case1.1: currnode only have 1 key:
                if len(currNode.key) == 1:
                    currNode.count += 1
                # case1.2: currNode have more than 1 key
                else:
                    currNode.key.remove(key)
                    newNode = LinkedListNode(key, 1)
                    newNode.prev = currNode
                    newNode.next = currNode.next
                    currNode.next.prev = newNode
                    currNode.next = newNode
                    self.count[key] = newNode
            else:
                # currNode.next != self.max and currNode.next.count == currNode.count + 1
                currNode.key.remove(key)
                currNode.next.key.append(key)
                self.count[key] = currNode.next
        self.printlinkedlist()

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.count:
            return

        currNode = self.count[key]
        if currNode.count == 1:
            # only have one element, remove the node:
            if len(currNode.key) == 1:
                self.min.next = currNode.next
                currNode.next.prev = self.min
            else:
                currNode.key.remove(key)
        else:
            if currNode.prev == self.min or currNode.prev.count != currNode.count - 1:
                if len(currNode.key) == 1:
                    currNode.count -= 1
                else:
                    currNode.key.remove(key)
                    newNode = LinkedListNode(key, 1)
                    newNode.next = currNode
                    newNode.prev = currNode.prev
                    currNode.prev.next = newNode
                    currNode.prev = newNode
                    self.count[key] = newNode
            else:
                currNode.key.remove(key)
                currNode.prev.key.append(key)
                self.count[key] = currNode.prev

        self.printlinkedlist()

    def printlinkedlist(self):
        if self.min.next == self.max:
            return None
        else:
            curr = self.min.next
            res = []
            while curr != self.max:
                print curr.count, curr.key
                res.append([curr.count, curr.key])
                curr = curr.next

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.max.prev == self.min:
            return ''
        else:
            return self.max.prev.key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.max.prev == self.min:
            return ''
        else:
            return self.min.next.key
        # return self.min.next.key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()