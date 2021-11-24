# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not (head or head.next):
            return True
        
        slow, fast = head, head.next
        
        # Find midpoint of linked list
        while fast:
            slow = slow.next
            fast = fast.next
            if (fast):
                fast = fast.next
        
        # Reverse second half of linked list starting from midpoint
        prev, cur = slow, slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Check for palindrome from both ends
        while prev != head:
            if prev.val != head.val:
                return False
            if head.next == prev:
                return True
            prev = prev.next
            head = head.next
        
        return True
            
        
