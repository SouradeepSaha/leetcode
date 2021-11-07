# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            temp = root.left
            if temp:
                while temp.right:
                    temp = temp.right

                temp.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
                
            
        
