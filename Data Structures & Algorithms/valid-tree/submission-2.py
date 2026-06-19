class Solution:
    #  time - O(V + E), space - O(V + E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # detect cycle
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)
        return len(visit) == n # detect connection