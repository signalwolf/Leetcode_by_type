# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverse(self, head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def add(self, l1, l2):
        dummyNode = ListNode(0)
        prev = dummyNode
        advance = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            prev.next = ListNode((num1 + num2 + advance) % 10)
            advance = (num1 + num2 + advance) / 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev = prev.next
        if advance:
            prev.next = ListNode(advance)
        return dummyNode.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Solution #1: reverse linked list and add then reverse again
        # Solution #2: get the num1, num2 and build num3 = num1 + num2 as linkedlist
        #   n1 = n1 * 10 + l1.val
        # Solution #3: get lens of both, move smaller one. DFS to add one by one, return with the advacne

        # S1: O(3 (m + n))
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        return self.reverse(self.add(l1, l2))

        # s2: O(3 (m + n))
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        num3 = num1 + num2
        num3 = map(int, list(str(num3)))
        dummyNode = ListNode(0)
        prev = dummyNode
        for i in xrange(len(num3)):
            prev.next = ListNode(num3[i])
            prev = prev.next
        return dummyNode.next

# Solution3:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution3(object):

    def addZero(self, n, head):
        while n:
            newHead = ListNode(0)
            newHead.next = head
            head = newHead
            n -= 1
        return head

    def add(self, h1, h2):
        if h1 == None and h2 == None: return 0, None

        advance, NextHead = self.add(h1.next, h2.next)

        currSum = h1.val + h2.val + advance
        currHead = ListNode(currSum % 10)
        currHead.next = NextHead
        return currSum / 10, currHead

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def getlen(head):
            res = 0
            while head:
                head = head.next
                res += 1
            return res

        len1, len2 = getlen(l1), getlen(l2)
        if len1 > len2:
            l2 = self.addZero(len1 - len2, l2)
        elif len1 < len2:
            l1 = self.addZero(len2 - len1, l1)

        # print len1, len2, getlen(l1), getlen(l2)

        advance, head = self.add(l1, l2)
        if advance:
            newHead = ListNode(advance)
            newHead.next = head
            return newHead
        else:
            return head
