# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        prev = dummyNode
        while l1 or l2:
            num1 = l1.val if l1 else float('inf')
            num2 = l2.val if l2 else float('inf')
            if num1 > num2:
                prev.next = l2
                l2 = l2.next if l2 else None
                prev = prev.next
            else:
                prev.next = l1
                l1 = l1.next if l1 else None
                prev = prev.next
        return dummyNode.next