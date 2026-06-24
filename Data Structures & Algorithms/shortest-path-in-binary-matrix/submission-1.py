class Solution:
    # time - O(n.m), space - O(n.m)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        wall = 1
        way = 0
        N = len(grid)
        if grid[0][0] == wall or grid[N-1][N-1] == wall:
            return -1
        
        directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        queue = deque([(0,0,1)])

        while queue:
            level = len(queue)
            for _ in range(level):
                row, col, length = queue.popleft()
                if (row == N-1 and col == N-1):
                    return length
                for dr, dc in directions:
                    mr = dr + row
                    mc = dc + col
                    if mr < 0 or mc < 0 or mr >= N or mc >= N or grid[mr][mc] != way:
                        continue
                    grid[mr][mc] = wall
                    queue.append((mr, mc, length + 1))
        return -1

