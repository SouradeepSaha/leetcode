# 113: Path Sum II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, curSum, tempArr):
        if root is None:
            return
        elif root.left is None and root.right is None:
            if curSum+root.val == self.targetSum:
                self.res.append([x for x in tempArr])
                self.res[-1].append(root.val)
        else:
            tempArr.append(root.val)
            self.dfs(root.left, curSum + root.val, tempArr)
            self.dfs(root.right, curSum + root.val, tempArr)
            tempArr.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.targetSum = targetSum
        self.dfs(root, 0, [])
        return self.res
