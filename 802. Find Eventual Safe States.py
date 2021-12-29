class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = collections.defaultdict(int) 
        
        # 0: Unvisited, -1: Currently Visiting, 1: visited
        def isSafe(node) -> bool:
            
            if visited[node] == -1:
                return False
            
            visited[node] = -1
            for edge in graph[node]:
                if visited[edge] == 1:
                    continue
                if edge == node or not isSafe(edge):
                    return False
            
            visited[node] = 1
            return True
        
        return filter(isSafe, range(len(graph)))
