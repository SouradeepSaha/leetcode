# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def findLen(head):
            res = 0
            while head:
                res += 1
                head = head.next
            return res
        
        lenA = findLen(headA)
        lenB = findLen(headB)
        diff = abs(lenA-lenB)
        
        for i in range(diff):
            if lenA >= lenB:
                headA = headA.next
            else:
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        
        return None
