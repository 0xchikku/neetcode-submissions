class Solution:
    # time - O(V+E), space - O(V+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visit = set()
        visit.add(0)
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        return len(visit) == n