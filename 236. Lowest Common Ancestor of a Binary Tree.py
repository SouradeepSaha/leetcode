#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.output = None
        
        def recurse(root):
            if not root:
                return 0
        
            mid = 1 if root.val == q.val or root.val == p.val else 0
            left = recurse(root.left)
            right = recurse(root.right)
            
            if mid+right+left >= 2:
                self.output = root
            
            return mid or left or right
        
        recurse(root)
        return self.output
        
