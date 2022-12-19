from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for u, v in edges:
          graph[u].add(v)
          graph[v].add(u)
        
        visited = set()

        def dfs(start):
          if start not in visited:
            visited.add(start)
            for vertex in graph[start]:
              dfs(vertex)
          
        dfs(source)
        return destination in visited
