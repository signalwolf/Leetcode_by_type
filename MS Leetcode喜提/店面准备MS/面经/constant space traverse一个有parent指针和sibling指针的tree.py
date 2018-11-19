# coding=utf-8
# 用constant space traverse一个有parent指针和sibling指针的tree，不能recursion，
# 不能建stack，不能修改树，

def traverse(root):
    res = [root.val]
    if root.left:
        curr = root.left
    else:
        curr = root.right

    while curr != root:
        res.append(curr.val)
        # have left child, go left
        if curr.left:
            curr = curr.left
        # have right child, go right
        elif curr.right:
            curr = curr.right
        # no left and right child but have right sibling:
        elif curr.sibling and curr != root and curr.sibling == curr.parent.right:
            curr = curr.sibling
        # no left, right child and don't have right sibling:
        # two cases:
            # curr is the right child of parent
            # curr don't have sibling
        # case 1 handle, move to parents till it have an right sibling
        # case 2 handle, move to parents till it have an right sibling
        else:
            while curr != root and (not curr.sibling or (curr.sibling and curr.sibling == curr.parent.left)):
                curr = curr.parent
            if curr != root:
                curr = curr.sibling
    return res