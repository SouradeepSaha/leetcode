# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLen(self, head: Optional[ListNode]) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l
        
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = self.findLen(head)
        rotations = k % l if l else 0
        
        # Handle the edge cases
        if l <= 1 or not rotations:
            return head
        
        count = 1
        headCopy = head
        while head:
            if count == l - rotations:
                newHead = head
            if not head.next:
                end = head
            head = head.next
            count += 1
        
        output = newHead.next
        newHead.next = None
        end.next = headCopy

        return output
