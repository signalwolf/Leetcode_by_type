# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def leafFinder(self, root, leaf):
        if not root.left and not root.right:
            leaf.append(root.val)
            return

        if root.left:
            self.leafFinder(root.left, leaf)

        if root.right:
            self.leafFinder(root.right, leaf)
        return

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        # find left path:
        curr = root.left
        left = []
        if curr:
            while (curr.left or curr.right):
                left.append(curr.val)
                curr = curr.left if curr.left else curr.right

        # find right path:
        curr = root.right
        right = []
        if curr:
            while curr.left or curr.right:
                right.append(curr.val)
                curr = curr.right if curr.right else curr.left

        leaf = []
        if root.left:
            self.leafFinder(root.left, leaf)
        if root.right:
            self.leafFinder(root.right, leaf)
        # print left, right, leaf
        return [root.val] + left + leaf + right[::-1]