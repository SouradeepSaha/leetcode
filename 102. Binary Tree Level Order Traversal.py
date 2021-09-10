# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 1)]
        ans = []
        curlevel = 0
        
        while len(queue):
            cur = queue.pop(0)
            if cur[0] is not None:
                if curlevel !=  cur[1]:
                    curlevel += 1
                    ans.append([])
                #print(cur)

                ans[-1].append(cur[0].val)
                queue.append((cur[0].left, cur[1]+1))
                queue.append((cur[0].right, cur[1]+1))

        return ans
