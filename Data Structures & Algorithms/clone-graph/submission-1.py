"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # time - O(V+E), space O(V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToNew[cur].neighbors.append(oldToNew[neighbor])
        
        return oldToNew[node]
