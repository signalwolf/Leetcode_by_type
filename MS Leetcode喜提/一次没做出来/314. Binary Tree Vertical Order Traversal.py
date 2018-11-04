# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 仔细思考，这道题就是要看出来可以设置index来解决问题。
from collections import defaultdict, deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = deque([[root, 0]])
        dicts = defaultdict(list)
        while queue:
            curr, index = queue.popleft()
            dicts[index].append(curr.val)
            if curr.left:
                queue.append([curr.left, index - 1])
            if curr.right:
                queue.append([curr.right, index + 1])
        res = []
        for i in sorted(dicts.keys()):
            res.append(dicts[i])
        return res


