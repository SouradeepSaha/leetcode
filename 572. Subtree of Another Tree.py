# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areSame(self, root, otherRoot):
        if root and otherRoot and root.val == otherRoot.val:
            return self.areSame(root.left, otherRoot.left) and self.areSame(root.right, otherRoot.right)
        if not root and not otherRoot:
            return True
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        res = self.areSame(root, subRoot)
        if not res and root:
            res = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return res
