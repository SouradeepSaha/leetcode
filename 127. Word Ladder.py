from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist = {word: 9999999 for word in wordList}
        dist[beginWord] = 1
        dq = deque()
        dq.append(beginWord)
        while len(dq):
            cur = dq.popleft()
            for index in range(len(cur)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = cur[:index] + char + cur[index+1:]
                    if newWord in dist and dist[newWord] > dist[cur] + 1:
                        dist[newWord] = dist[cur] + 1
                        if newWord == endWord:
                            return dist[newWord]
                        dq.append(newWord)
        
        return 0
