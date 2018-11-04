# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        mapping = {}
        curr = head
        # generate the mapping between current linked list and target:
        while curr:
            copy_curr = RandomListNode(curr.label)
            mapping[curr] = copy_curr
            curr = curr.next
        curr = head
        # copy the random pointer and the next pointer
        while curr:
            original, copy = curr, mapping[curr]

            # copy random pointer:
            if original.random:
                copy.random = mapping[original.random]

            # copy next pointer:
            if original.next:
                copy.next = mapping[original.next]

            curr = curr.next
        return mapping[head] if head else None
