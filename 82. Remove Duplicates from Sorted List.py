# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        prev = None
        deleted = False
        
        while 1:
            if fast is None:
                if deleted:
                    if prev is None:
                        head = None
                    else:
                        prev.next = None
                break
            
            if slow.val == fast.val:
                deleted = True
            
            else:
                if deleted:
                    deleted = False
                    if prev is None:
                        head = fast
                    else:
                        prev.next = fast
                    slow = fast
                else:
                    prev = slow
                    slow = slow.next
            
            fast = fast.next
        return head
