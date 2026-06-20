class Solution:
    # # Time: O(E * α(V)), Space: O(V) - where α(V) is the inverse Ackermann function (effectively constant).
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [i for i in range(N+1)]
        height = [0] * (N+1)
       
        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
                
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            
            if height[root1] < height[root2]:
                parents[root1] = root2
            elif height[root1] > height[root2]:
                parents[root2] = root1
            else:
                parents[root2] = root1
                height[root1] += 1
            
            return True


        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        
        return [-1,-1]
