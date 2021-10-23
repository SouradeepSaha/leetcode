import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        heap = []
        head = cur = ListNode(None)
        
        for l in lists:
            if l:
                heapq.heappush(heap, Wrapper(l))
                
        while len(heap):
            top = heapq.heappop(heap)
            if top.node.next:
                heapq.heappush(heap, Wrapper(top.node.next))
            
            cur.next = top.node
            cur = cur.next
        
        return head.next
                
