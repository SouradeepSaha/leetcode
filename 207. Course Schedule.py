# 207. Course Schedule
# Topological Sort
from typing import List
from collections import defaultdict

class Solution:
    def topSort(self, visited: dict, cur: int, adj_list: dict):
        if cur not in visited or visited[cur] == 1:
            return True
        
        if visited[cur] == 0:
            return False
        
        visited[cur] = 0

        for node in adj_list[cur]:
            if not self.topSort(visited, node, adj_list):
                return False
        visited[cur] = 1

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, adj_list = dict(), defaultdict(list)

        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])
            visited[edge[0]] = -1

        for k in visited.keys():
            if not self.topSort(visited, k, adj_list):
                return False
        return True
