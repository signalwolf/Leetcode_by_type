# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, n1, n2):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == n1 or root == n2:
            return root

        left = self.lowestCommonAncestor(root.left, n1, n2)
        right = self.lowestCommonAncestor(root.right, n1, n2)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None