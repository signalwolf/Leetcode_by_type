

def helper(root, visited):
    if root in visited:
        return visited[root]
    if root == None:
        return 0

    # choice root:
    choice_root = root.val
    if root.left:
        choice_root += helper(root.left.left, visited) + helper(root.left.right, visited)

    if root.right:
        choice_root += helper(root.right.left, visited) + helper(root.right.right, visited)

    no_root = helper(root.left, visited) + helper(root.right, visited)
    visited[root] = max(no_root, choice_root)
    return visited[root]

def houseRobber(root):
    helper(root, {})