from string import ascii_lowercase

class TrieNode:
    def __init__(self):
        self.ends = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            
            root = root.children[char]
        root.ends = True
    
    def findSuggestions(self, trienode, prev):
        res = []
        def dfs(node, cur):
            #print(cur)
            if len(res) >= 3:
                return
            if node.ends:
                res.append(cur)
            
            for char in ascii_lowercase: 
                if char in node.children:
                    dfs(node.children[char], cur+char)
            
        dfs(trienode, prev)
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        for product in products:
            trie.addWord(product)
        
        res = []
        curnode = trie.root
        curword = ""
        
        rem = len(searchWord)
        for char in searchWord:
            if char not in curnode.children:
                break
            rem -= 1
            curword += char
            curnode = curnode.children[char]
            res.append(trie.findSuggestions(curnode, curword))
        
        for i in range(rem):
            res.append([])
        
        return res
        
        
