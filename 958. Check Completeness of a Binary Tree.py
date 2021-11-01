from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dq1, dq2 = deque(), deque()
        dq1.append(root)
        found, level, count = False, 0, 0
        
        while len(dq1):
            top = dq1.popleft()
            if top:
                if not found:
                    found = True
                count += 1
                dq2.append(top.right)
                dq2.append(top.left)
                
            elif found:
                return False
            
            if not len(dq1):
                while len(dq2) and not dq2[0]:
                    dq2.popleft()
                if count < int(pow(2, level)) and len(dq2):
                    return False
                dq1, dq2, count, found = dq2, deque(), 0, False
                level += 1
                
        return True
                
        
        
