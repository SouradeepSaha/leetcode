# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderHash = dict()
        for index, item in enumerate(inorder):
            inorderHash[item] = index
        
        postPtr = len(postorder)-1
        def listToBST(leftPtr, rightPtr):
            nonlocal postPtr
            if postPtr < 0 or rightPtr < leftPtr:
                return None
            cur = postorder[postPtr]

            postPtr -= 1
            mid = inorderHash[cur]
            right = listToBST(mid+1, rightPtr)
            left = listToBST(leftPtr, mid-1)
            return TreeNode(cur, left, right)
        
        return listToBST(0, len(postorder)-1)
        
