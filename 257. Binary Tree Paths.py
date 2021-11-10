# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        def dfs(root, cur):
            if root.left:
                dfs(root.left, cur + str(root.val) +"->")
            if root.right:
                dfs(root.right, cur+str(root.val) +"->")
            
            if not root.left and not root.right:
                output.append(cur + str(root.val))
        
        dfs(root, "")
        return output
