from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output, found = [], False 
        dq1, dq2 = deque(), deque()
        dq1.append(root)
        while len(dq1):
            top = dq1.popleft()
            if top:
                if not found:
                    found = True
                    output.append(top.val)
                
                dq2.append(top.right)
                dq2.append(top.left)
            
            if not len(dq1):
                dq1, dq2, found = dq2, deque(), False
                
        return output
