# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs_sum(self, root, temp, target):
        cur = temp+root.val
        if not root.left and not root.right:
            return cur == target
        else:
            left, right = False, False
            if root.left:
                left = self.dfs_sum(root.left, cur, target)
            if root.right:
                right = self.dfs_sum(root.right, cur, target)
            return left or right
        
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs_sum(root, 0, targetSum) if root else False
