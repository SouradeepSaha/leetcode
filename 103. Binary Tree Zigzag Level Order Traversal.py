from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output, temp = [], []
        
        if not root:
            return output
        
        leftRight, rightLeft = deque(), deque()
        leftRight.append(root)
        uselr, userl = True, False
        
        while len(leftRight) or len(rightLeft):
            if uselr:
                top = leftRight.pop()
                temp.append(top.val)
                if top.left:
                    rightLeft.append(top.left)
                if top.right:
                    rightLeft.append(top.right)
                if not len(leftRight):
                    output.append(temp)
                    userl, uselr, temp = True, False, []

            else:
                top = rightLeft.pop()
                temp.append(top.val)
                if top.right:
                    leftRight.append(top.right)
                if top.left:
                    leftRight.append(top.left)
                if not len(rightLeft):
                    output.append(temp)
                    userl, uselr, temp = False, True, []

        return output
                
        
        
