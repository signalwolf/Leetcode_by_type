from collections import deque
def depthofBinaryTree(root):
    # BFS, DFS
    # DFS: 36ms
    if root == None: return 0
    return max(depthofBinaryTree(root.left), depthofBinaryTree(root.right)) + 1

    # BFS:32ms
    if root == None: return 0
    depth = 0
    queue = deque([root])
    while queue:
        next_level = deque()
        depth += 1
        while queue:
            curr = queue.popleft()
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
        queue = next_level
    return depth