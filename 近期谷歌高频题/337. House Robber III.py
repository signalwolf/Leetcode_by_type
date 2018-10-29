
# optimized 1: 44ms, 60%
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


# optimized 2: 44ms, 60%
def houseRobber2(root):
    return max (helper2 (root))

def helper2(root):
    if root == None: return [0, 0]
    left = helper2(root.left)
    right = helper2(root.right)
    ans = [0] * 2
    ans[0] = max(left) + max(right)
    ans[1] = root.val + left[1] + right[1]
    return ans