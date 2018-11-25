
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def cloneTree(root):
    # BFS, build left and right child, then connect the root to left and right.

    if not root: return None

    CopyRoot = TreeNode(root.val)
    queue = deque()
    queue.append(root)
    mapping = {root: CopyRoot}
    while queue:
        # step1: generate the left and right then connect it with copy one:
        curr = queue.popleft()
        CopyLeft, CopyRight = None, None
        if curr.left:
            CopyLeft = TreeNode(curr.left.val)
            mapping[curr.left] = CopyLeft
            queue.append(curr.left)
        if curr.right:
            CopyRight = TreeNode(curr.right.val)
            mapping[curr.right] = CopyRight
            queue.append(curr.right)
        currCopy = mapping[curr]
        currCopy.left = CopyLeft
        currCopy.right = CopyRight
        # step2: update it to queue to continue BFS
    return CopyRoot




def buildBST(arr, start, end):
    if start >= end: return None
    if start == end - 1: return TreeNode(arr[start])
    mid = start + (end - start ) / 2
    root = TreeNode(arr[mid])
    root.left = buildBST(arr, start, mid)
    root.right = buildBST(arr, mid + 1, end)
    return root

from random import randint

def pre_order_stack(root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def main():
    lens = 20
    ans = set()
    for i in xrange(lens):
        ans.add(randint(0, 100))
    arr = sorted(list(ans))
    root = buildBST(arr, 0, len(arr) - 1)
    CopyRoot = cloneTree(root)
    print pre_order_stack(root)
    print pre_order_stack(root) == pre_order_stack(CopyRoot)

if __name__ == '__main__' :
    main()