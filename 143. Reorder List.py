# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        if not fast or not fast.next:
            return
        
        while fast.next:
            slow = slow.next
            fast = fast.next.next if fast.next.next else fast.next
        
        prev, slow = slow, slow.next
        prev.next = None
        while slow:
            right = slow.next
            slow.next = prev
            prev = slow
            slow = right
            
        left, right = head, prev
        while left is not right:
            leftnext, rightnext = left.next, right.next
            
            left.next = right
            right.next = left = leftnext
            right = rightnext
            
            if right.next is left:
                left.next, right.next = right, None
                break
                
        
