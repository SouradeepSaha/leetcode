# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def recursiveRev(self, cur, prev):
        if cur is None:
            return prev
        return self.recursiveRev(cur.next, ListNode(cur.val, next=prev))
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveRev(head, None)
        
