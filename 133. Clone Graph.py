from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        stack = deque()
        visited = set()
        root = Node(node.val, node.neighbors)
        nodes = {node.val: root}
        stack.append(root)
        
        while len(stack):
            cur = stack.pop()
            if cur.val not in visited:
                visited.add(cur.val)
                newNeighbors = []
                for neighbor in cur.neighbors:
                    if neighbor.val in nodes:
                        newNeighbors.append(nodes[neighbor.val])
                    else:
                        newNeighbor = Node(neighbor.val, neighbor.neighbors)
                        newNeighbors.append(newNeighbor)
                        nodes[newNeighbor.val] = newNeighbor
                        stack.append(newNeighbor)

                cur.neighbors = newNeighbors

        return root
