# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postOrder(self, root, lst):
        if not root:
            return
        self.postOrder(root.left, lst)
        self.postOrder(root.right, lst)
        lst.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.postOrder(root, lst)
        return lst
