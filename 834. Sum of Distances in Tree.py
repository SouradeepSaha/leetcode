from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        dp = {}
        result = [0 for i in range(n)]

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            dp[edge[0]] = []
            dp[edge[1]] = []
        
        visited = set()
        # Preprocess the input to store the number of children 
        # and the path sum of the subtree starting at each individual node
        def preprocess(start):
            visited.add(start)
        
            children, pathsum = 1, 0
            for vertex in graph[start]:
                if vertex not in visited:
                    preprocess(vertex)
                    children += dp[vertex][0]
                    pathsum += dp[vertex][1] + dp[vertex][0]
            
            dp[start] = (children, pathsum)
        
        preprocess(0)
        visited = set()
        result[0] = dp[0][1]
        print(dp)
        
        # Use the dp array to calculate the result
        # The path sum for each node is the path sum for its parent
        # adjusted with the number of nodes getting farther or closer
        def dfs(start):
            visited.add(start)
            for vertex in graph[start]:
                if vertex not in visited:
                    result[vertex] = result[start]-dp[vertex][0]+(dp[0][0]-dp[vertex][0])
                    dfs(vertex)
        
        
        dfs(0)
        return result

        # Time complexity: O(n)
        # n = Number of nodes given in input
