# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            next_level_node = deque([])
            curr_level_res = []
            while queue:
                curr = queue.popleft()
                curr_level_res.append(curr.val)
                if curr.left:
                    next_level_node.append(curr.left)
                if curr.right:
                    next_level_node.append(curr.right)
            if len(res) % 2 == 0:
                res.append(curr_level_res)
            else:
                res.append(curr_level_res[::-1])
            queue = next_level_node
        return res