# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeights(self, root: Optional[TreeNode]):
        output = [0,0]
        copy = root
        while root:
            root = root.left
            output[0] += 1
        
        root = copy
        while root:
            root = root.right
            output[1] += 1
        
        
        return output
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        heights = self.findHeights(root)
        #print(heights)
        if heights[0] == heights[1]:
            return pow(2, heights[0])-1
        
        return self.countNodes(root.left) + self.countNodes(root.right)+1
        
        
