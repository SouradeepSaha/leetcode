from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = {}
        graph = defaultdict(set)
        for edge in dislikes:
            color[edge[0]] = -1
            color[edge[1]] = -1
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        

        def isBipartite(start):
            queue = deque([])
            color[start] = 0
            queue.append(start)
            
            while len(queue):
                top = queue.popleft()
                for vertex in graph[top]:
                    if color[top] == color[vertex]:
                        return False
                    elif color[vertex] == -1:
                        color[vertex] = not color[top]
                        queue.append(vertex)
            
            return True
        
        for i in range(1, n):
            if i in color and color[i] == -1:
                if not isBipartite(i):
                    return False
        
        return True



