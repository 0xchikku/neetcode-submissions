class Solution:
    # time - O(n^2), space - O(n^2)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        clean = 0
        block = 1
        if grid[0][0] == block:
            return -1

        N = len(grid)
        end = (N - 1, N - 1)
        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        queue = deque([(0,0,1)])
        visit = set((0,0))

        while queue:
            row, col, length = queue.popleft()
            if (row, col) == end:
                return length
            for dr, dc in directions:
                mr, mc = dr + row, dc + col
                
                if (mr < 0 or mc < 0 or mr >= N or mc >= N or grid[mr][mc] == block or (mr, mc) in visit):
                    continue
                queue.append((mr, mc, length+1))
                visit.add((mr, mc))

        return -1

        
