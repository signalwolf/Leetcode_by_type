# coding=utf-8

#binary tree lowest common ancestor，说方法就行了

# Leetcode: 90.47%
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

def LCA(root, n1, n2):
    if root == n1:
        return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)
    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None