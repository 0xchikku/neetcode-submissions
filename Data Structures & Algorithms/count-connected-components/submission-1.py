class Solution:
    # time - O(V+E), space - O(V+E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = [False] * n
        count = 0

        def bfs(node):
            visited[node] = True
            queue = deque([node])

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    queue.append(neighbor)

        for node in range(n):
            if not visited[node]:
                bfs(node)
                count += 1
        
        return count