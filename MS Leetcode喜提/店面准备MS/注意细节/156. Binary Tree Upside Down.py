# coding=utf-8
# 注意在计算path的时候，到了root点就需要变化

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root

        path = []
        while root:
            path.append(root)
            root = root.left

        newRoot = path[-1]
        #
        while len(path) != 1:
            curr = path.pop()
            curr.left = path[-1].right
            curr.right = path[-1]

        path[0].left = path[0].right = None
        return newRoot
