class Node:
    # Note: adding the children as a dict
    # mutates the original dict
    def __init__(self, char = None):
        self.char = char
        self.end = False
        self.children = dict()
    
class WordDictionary:

    def __init__(self):
        self.trie = Node()
        
    def addWord(self, word: str) -> None:
        root = self.trie
        for index, char in enumerate(word):
            if char not in root.children:
                root.children[char] = Node(char)
            root = root.children[char]
            if index == len(word)-1:
                root.end = True
        
    def search(self, word: str) -> bool:
        
        def dfs(index, root)->bool:
            if index >= len(word):
                return root.end
            
            if word[index] != '.':
                if word[index] in root.children:
                    return dfs(index+1, root.children[word[index]])
                return False
            
            found = False
            for key in root.children.keys():
                found = found or dfs(index+1, root.children[key])
                if found:
                    return True
            
            return False
        return dfs(0, self.trie)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
