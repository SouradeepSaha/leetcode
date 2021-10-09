# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, newhead = None, head
        while head:
            if head.val == val:
                if prev:
                    prev.next = head.next
                else:
                    newhead = head.next
            else:
                prev = head
            head = head.next
            
        return newhead
            
