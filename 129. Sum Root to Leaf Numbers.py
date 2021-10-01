# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total = 0
    
    def dfs_sum(self, root, temp):
        temp2 = temp + str(root.val)
        if root.left:
            self.dfs_sum(root.left, temp2)
        if root.right:
            self.dfs_sum(root.right, temp2)
        if not root.left and not root.right:
            self.total += int(temp2)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs_sum(root, "")
        return self.total
        
        
