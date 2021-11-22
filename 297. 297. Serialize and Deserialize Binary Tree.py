# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = ""
        if root:
            output += str(root.val) + ','
            output += self.serialize(root.left) + ','
            output += self.serialize(root.right)
        
        return output    
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        index = 0
        def parse():
            nonlocal index
            if arr[index] == "":
                index += 1
                return None
        
            root = TreeNode(arr[index])
            index += 1
            root.left = parse()
            root.right = parse()
            
            return root
        
        return parse()
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
