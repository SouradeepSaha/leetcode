class Solution:
    def bfs(self, graph, color, start) -> bool:
        q = [start]
        color[start] = 0
        
        while len(q):
            top = q.pop(0)
            for node in graph[top]:
                if color[node] == color[top]:
                    return False
                if color[node] == -1:
                    color[node] = not color[top]
                    q.append(node)
        return True
            
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]
        
        for i in range(len(graph)):
            if color[i] == -1 and not self.bfs(graph, color, i):
                return False
            print(color)
            
        return True
