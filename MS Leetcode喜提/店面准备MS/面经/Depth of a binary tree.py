
def depthofBinaryTree(root):
    # BFS, DFS
    # DFS:
    if root == None: return 0
    return max(depthofBinaryTree(root.left), depthofBinaryTree(root.right)) + 1