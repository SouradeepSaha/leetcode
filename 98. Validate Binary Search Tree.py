# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root) ->bool:
        if not root:
            return True
        if not self.inorder(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.inorder(root.right)
            
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        return self.inorder(root)
    
    # Iterative Solution
    def isValidBST2(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
