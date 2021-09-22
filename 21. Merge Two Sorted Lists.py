# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        res, cur = None, None
        
        while l1 and l2:
            val = None
            if l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
                
            if not res:
                res = ListNode(val)
                cur = res
            else:
                new_node = ListNode(val)
                cur.next = new_node
                cur = new_node
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
            
        return res
                
            
        
