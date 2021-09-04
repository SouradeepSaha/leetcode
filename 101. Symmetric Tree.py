# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isEqual(self, ltree, rtree):
      if ltree is None and rtree is None:
        return True
      if ltree is not None and rtree is not None:
        if ltree.val == rtree.val:
          # Note that we need to switch the order for mirror image
          return self.isEqual(ltree.left, rtree.right) and self.isEqual(ltree.right, rtree.left)
        
      return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      if root.left is None and root.right is None:
        return True
      if root.left is not None and root.right is not None:
        return self.isEqual(root.left, root.right)
      return False
      
        
