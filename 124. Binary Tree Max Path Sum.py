# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    maxSum = -99999

    def postorder(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            if Solution.maxSum < root.val:
                Solution.maxSum = root.val
            return root.val

        leftSum = max(self.postorder(root.left), 0)
        rightSum = max(self.postorder(root.right), 0)
        sum = leftSum + rightSum + root.val

        if sum > Solution.maxSum:
            Solution.maxSum = sum
        return root.val + max(leftSum, rightSum)

    def maxPathSum(self, root: TreeNode) -> int:
        Solution.maxSum = -999999
        self.postorder(root)
        return Solution.maxSum

