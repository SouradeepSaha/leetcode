# Time Complexity: O(V), V = Number of Nodes in Graph
# Space Complexity: O(V)

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_list = defaultdict(set)
        
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
            
        cur_leaves = []
        for key in adj_list.keys():
            if len(adj_list[key]) == 1:
                cur_leaves.append(key)

        rem = n
        while rem > 2:
            rem -= len(cur_leaves)
            new_leaves = []
            
            while len(cur_leaves):
                cur = cur_leaves.pop()
                neighbour = adj_list[cur].pop() # remove the element from the set
                adj_list[neighbour].remove(cur)
                if len(adj_list[neighbour]) == 1:
                    new_leaves.append(neighbour)
                del adj_list[cur]
            cur_leaves = new_leaves
        
        return cur_leaves
            
