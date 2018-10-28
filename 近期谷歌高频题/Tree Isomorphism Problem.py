# coding=utf-8
# time complexity: O(mn)

# 注意考虑边界条件：root1 == None and root2 == None....
def isomorphism (root1, root2):
    # in each condition, it can be root1.left match to root2.right
    # or root1.left match to root2.left
    if root1 == None and root2 == None: return True
    if root1 == None or root2 == None: return False
    if root1.val == root2.val:
        return (isomorphism(root1.left, root2.left) and isomorphism(root1.right, root2.right)) \
               or (isomorphism(root1.left, root2.right) and isomorphism(root1.right, root2.left))
    return False