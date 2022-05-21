class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word):
        cur = self
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Trie()
            cur = cur.children[letter]
        cur.isWord = True

    def removeWord(self, word, node=None):
        if not node:
            node = self
        if word == "":
            node.isWord = False
            return

        newnode = node.children[word[0]]
        self.removeWord(word[1:], newnode)
        if not newnode.isWord and len(newnode.children) == 0:
            del node.children[word[0]]


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.addWord(word)

        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(board), len(board[0])

        result, visited, added = set(), set(), set()
        wordLst = []

        def dfs(row, col, node):
            # print(row, col, word)
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and board[row][col] in node.children:
                wordLst.append(board[row][col])
                visited.add((row, col))
                if node.children[board[row][col]].isWord:
                    newWord = "".join(wordLst)
                    result.add(newWord)
                    trie.removeWord(newWord)
                for move in moves:
                    if board[row][col] in node.children:
                        dfs(row + move[0], col + move[1], node.children[board[row][col]])
                visited.remove((row, col))
                wordLst.pop()

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)

        return list(result)

    '''
sol = Solution()
print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"]))'''
