# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = dict()
        self.preorder_ind = 0
        for ind, val in enumerate(inorder):
            index[val] = ind
        
        def recurse(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.preorder_ind]
            root_ind = index[root_val]
            self.preorder_ind += 1

            return TreeNode(root_val, recurse(left, root_ind-1), recurse(root_ind+1, right))
        
        return recurse(0, len(preorder)-1)
                
