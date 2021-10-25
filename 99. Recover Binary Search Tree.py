# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        cur, prev, drops = root, TreeNode(-math.inf), []

        while cur:
            if cur.left:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right

                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                    continue

                pred.right = None

            if cur.val < prev.val:
                drops.append((prev, cur))

            prev = cur
            cur = cur.right

        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
        

            
