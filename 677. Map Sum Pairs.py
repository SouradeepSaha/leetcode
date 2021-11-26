class Node:
    def __init__(self):
        self.children = dict()
        self.val = None
        
class MapSum:
    def __init__(self):
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        root = self.root
        
        for ind, c in enumerate(key):
            if c not in root.children:
                root.children[c] = Node()
            
            if ind == len(key)-1:
                root.children[c].val = val
            
            root = root.children[c]
            
    def sum(self, prefix: str) -> int:
        root, output = self.root, 0
        for c in prefix:
            if c not in root.children:
                return 0
            root = root.children[c]
        
        def dfs(root):
            nonlocal output
            if root.val:
                output += root.val
            for node in root.children.keys():
                dfs(root.children[node])
        
        dfs(root)
        return output

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
