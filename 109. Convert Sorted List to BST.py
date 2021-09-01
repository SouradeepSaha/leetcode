from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        prev, fast, slow = None, head, head

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                prev = slow
                slow = slow.next

        prev.next = None
        return TreeNode(slow.val, left=self.sortedListToBST(head), right=self.sortedListToBST(slow.next))
