# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                return None
            
            if root.left and root.right:
                temp = root.left
                while (temp.right):
                    temp = temp.right
                
                return TreeNode(temp.val, self.deleteNode(root.left, temp.val), root.right)
                
            
            return root.left if not root.right else root.right
        
        elif key < root.val:
            return TreeNode(root.val, self.deleteNode(root.left, key), root.right)
        
        return TreeNode(root.val, root.left, self.deleteNode(root.right, key))
            
