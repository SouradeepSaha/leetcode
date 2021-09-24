"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None:
            return 0
        
        depth=1
        max_depth=0    
        for  child in root.children:
            child_depth = self.maxDepth(child)
            max_depth = max(max_depth, child_depth)
        return depth+max_depth
        
