class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths = []
        n = len(graph)

        def dfs(start, curpath):
            curpath.append(start)

            if start == n-1:
                paths.append([v for v in curpath])

            else:
                for vertex in graph[start]:
                    dfs(vertex, curpath)
            
            curpath.pop()
        
        dfs(0, [])
        return paths
