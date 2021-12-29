class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def bfs(node):
            q = collections.deque()
            q.append(node)
            while len(q):
                top = q.popleft()
                if top not in visited:
                    visited.add(top)
                    for index, val in enumerate(isConnected[top]):
                        if val and index != top:
                            q.append(index)
        
        comp = 0
        for node in range(len(isConnected)):
            #print(visited)
            if node not in visited:
                comp += 1
                bfs(node)
        
        return comp
