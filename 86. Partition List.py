# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        largeListStart = largeListEnd = ListNode(0)
        smallListStart = smallListEnd = ListNode(0)
        
        while head:
            if head.val >= x:
                largeListEnd.next = head
                largeListEnd = largeListEnd.next

            else:
                smallListEnd.next = head
                smallListEnd = smallListEnd.next
            
            head = head.next

        
        largeListEnd.next = None
        smallListEnd.next = largeListStart.next
        return smallListStart.next
