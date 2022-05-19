# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for index, val in enumerate(postorder):
            indices[val] = index
        
        def recurse(preL, preR, postL):
            if preL > preR:
                return None
            root = TreeNode(preorder[preL])
            if preR-preL > 0:
                leftTreeLen = indices[preorder[preL+1]] - postL
                root.left = recurse(preL+1, preL+1+leftTreeLen, postL)
                root.right = recurse(preL+leftTreeLen+2, preR, postL+leftTreeLen+1)
            
            return root
        
        return recurse(0, len(preorder)-1, 0)
