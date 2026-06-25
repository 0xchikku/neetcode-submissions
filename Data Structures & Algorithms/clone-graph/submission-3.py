"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def dfs(self, node):
        copies = {}

        def createCopy(node):
            if node in copies:
                return copies[node]
            
            copy = Node(node.val)
            copies[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(createCopy(neighbor))
            
            return copy
        
        return createCopy(node)
    
    def bfs(self, node):
        copies = {}
        copy = Node(node.val)
        copies[node] = copy
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in copies:
                    copy = Node(neighbor.val)
                    copies[neighbor] = copy
                    queue.append(neighbor)
                copies[cur].neighbors.append(copies[neighbor])
        return copies[node]



    # time - O(V+E), space - O(V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        # return self.dfs(node)
        return self.bfs(node)
