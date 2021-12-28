from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        visited = [-1 for _ in range(numCourses)]
        
        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])
        
        output = []
        
        def topSort(course: int) -> bool:
            if visited[course] == 0:
                return False
            
            if visited[course] == 1:
                return True
            
            visited[course] = 0
            for prereq in adj_list[course]:
                if not topSort(prereq):
                    return False
            
            visited[course] = 1
            output.append(course)
            return True
        
        for course in range(numCourses):
            if visited[course] == -1:
                if not topSort(course):
                    return []
        
        return output
