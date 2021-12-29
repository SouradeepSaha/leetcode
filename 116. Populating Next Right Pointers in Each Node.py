"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def addNext(cur, nextright):
            if cur:
                cur.next = nextright
                
                addNext(cur.left, cur.right)
                addNext(cur.right, nextright.left if nextright else nextright)
        
        addNext(root, None)
        return root
