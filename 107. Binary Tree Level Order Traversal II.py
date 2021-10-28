from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findHeight(self, root):
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right)) if root else 0
    
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = [[] for i in range(self.findHeight(root))]  
        dq1, dq2 = deque(), deque()
        dq1.append(root)
        ind = len(output)-1
        
        while len(dq1):
            top = dq1.pop()
            if top:
                output[ind].append(top.val)
                dq2.appendleft(top.left)
                dq2.appendleft(top.right)

            if not len(dq1):
                dq1 = dq2
                ind -= 1
                dq2 = deque()
                    
        return output
            
