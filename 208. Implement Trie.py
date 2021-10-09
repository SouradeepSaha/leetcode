class Trie:      
    class Node:
        def __init__(self):
            self.val = None
            self.end = False
            self.children = dict()
    
    def __init__(self):
        self.trie = self.Node()
        
    def insert(self, word: str) -> None:
        root = self.trie
        for i in range(len(word)):
            if word[i] in root.children:
                if i == len(word)-1:
                    root.children[word[i]].end = True
                root = root.children[word[i]]
            else:
                root.children[word[i]] = self.Node()
                root.children[word[i]].end= False if i != len(word)-1 else True
                root = root.children[word[i]]

    def search(self, word: str) -> bool:
        root = self.trie
        for i in range(len(word)):
            if word[i] in root.children:
                if i == len(word)-1:
                    return root.children[word[i]].end
                root = root.children[word[i]]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for i in range(len(prefix)):
            if prefix[i] in root.children:
                root = root.children[prefix[i]]
            else:
                return False
        return True
