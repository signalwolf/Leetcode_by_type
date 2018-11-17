# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        prev = head
        advance = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            curr = ListNode((num1 + num2 + advance) % 10)
            advance = (num1 + num2 + advance) / 10
            prev.next = curr
            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if advance:
            curr = ListNode(advance)
            prev.next = curr
        return head.next
