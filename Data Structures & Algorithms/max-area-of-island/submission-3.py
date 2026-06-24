class Solution:
    # time - O(n.m), space - O(n.m)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        water = 0
        land = 1
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        maxArea = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != land:
                return 0

            grid[row][col] = water
            area = 1
            for dr, dc in directions:
                mr = dr + row
                mc = dc + col
                area += dfs(mr, mc)
            return area
        
        def bfs(row, col):
            area = 1
            grid[row][col] = water
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    mr = row + dr
                    mc = col + dc
                    if mr < 0 or mc < 0 or mr >= rows or mc >= cols or grid[mr][mc] != land:
                        continue
                    area += 1
                    grid[mr][mc] = water
                    queue.append((mr, mc))
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land:
                    area = dfs(row, col)
                    # area = bfs(row, col)
                    maxArea = max(area, maxArea)
        
        return maxArea
