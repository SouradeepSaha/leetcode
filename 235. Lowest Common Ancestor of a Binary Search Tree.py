# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def BSTcontains(root: TreeNode, node: TreeNode):
    if root is None:
        return False
    if root.val == node.val:
        return True
    elif root.val > node.val:
        return BSTcontains(root.left, node)
    return BSTcontains(root.right, node)


class Solution:
    lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if self.lca is None:
            self.lca = root

        if BSTcontains(root.left, p) and BSTcontains(root.left, q):
            self.lca = root.left
            return self.lowestCommonAncestor(root.left, p, q)

        elif BSTcontains(root.right, p) and BSTcontains(root.right, q):
            self.lca = root.right
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return self.lca
