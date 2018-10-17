# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def printLinkedList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print res

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return head
        if not head.next: return TreeNode(head.val)
        slow, fast = head, head.next.next
        # smart: 通过让fast先走两步，这使slow停在了mid 的前一位，这样省去了让prev不断向前的过程
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        root = TreeNode(mid.val)
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

