# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def dfs(self, root)-> int:
        if root is None:
            return 0
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return -1 if abs(l-r) > 1 or l==-1 or r == -1 else 1+max(l, r)
            
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.dfs(root) == -1 else True
