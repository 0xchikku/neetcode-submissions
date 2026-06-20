class Solution:
    # time - O(V+E), space - O(V+E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = [False] * n 
        count = 0
        
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)

        for node in range(n):
            if not visited[node]:
                dfs(node)
                count += 1
        
        return count
