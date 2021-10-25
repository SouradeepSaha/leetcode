# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.arr
    
    # Morris Inorder Traversal
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        cur = root
        
        while cur:
            print(cur.val)
            if not cur.left:
                output.append(cur.val)
                cur = cur.right
            
            else:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right
                
                # Creating the link
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                    
                # Removing the previous link
                elif pred.right is cur:
                    pred.right = None
                    output.append(cur.val)
                    cur = cur.right
        
        return output
