# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preOrder(self, root, lst):
        if not root:
            return
        lst.append(root.val)
        self.preOrder(root.left, lst)
        self.preOrder(root.right, lst)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.preOrder(root, lst)
        return lst
