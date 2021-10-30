from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leftPos, maxwidth = dict(), 0
        
        def findWidth(root, level, pos):
            nonlocal leftPos, maxwidth
            if root:
                if level not in leftPos:
                    leftPos[level] = pos
                
                maxwidth = max(maxwidth, pos-leftPos[level]+1)
                findWidth(root.left, level+1, pos*2)
                findWidth(root.right, level+1, pos*2+1)
        
        findWidth(root, 0, 0)
        return maxwidth
                    
