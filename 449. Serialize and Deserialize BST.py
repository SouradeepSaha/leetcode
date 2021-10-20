# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        def preorder(root, arr):
            if root:
                arr.append(str(root.val))
                preorder(root.left, arr)
                preorder(root.right, arr)
        
        preorder(root, arr)
        return ",".join(arr)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """  
        if not len(data):
            return None
        
        preorder = list(map(int, data.split(",")))
        index = 0
        
        def recurse(preorder, maxBound):
            nonlocal index
            
            if index >= len(preorder) or preorder[index] > maxBound:
                return None
            
            root = TreeNode(preorder[index])
            index += 1
            root.left=recurse(preorder, root.val)
            root.right=recurse(preorder, maxBound)
            return root
        
        return recurse(preorder, math.inf)
            
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
#print(tree)
# ans = deser.deserialize(tree)
# return ans
