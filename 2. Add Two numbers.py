# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    carry = 0
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = self.carry
        
        if l1 is None and l2 is None:
          return ListNode(self.carry) if self.carry else None
        
        if l1 is not None:
          sum += l1.val
        
        if l2 is not None:
          sum += l2.val
          
        self.carry = int(sum / 10)
        sum = sum % 10
        
        return ListNode(val = sum, next = self.addTwoNumbers(l1=l1.next if l1 else None, l2=l2.next if l2 else None))
