# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0
        
        def recurse(preorder, maxBound):
            nonlocal index
            
            if index >= len(preorder) or preorder[index] > maxBound:
                return None
            root = TreeNode(preorder[index])
            index += 1
            root.left=recurse(preorder, root.val)
            root.right=recurse(preorder, maxBound)
            return root
        
        return recurse(preorder, math.inf)
