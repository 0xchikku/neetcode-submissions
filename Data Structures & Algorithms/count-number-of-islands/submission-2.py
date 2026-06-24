class Solution:
    # time - O(n.m), space - O(n.m)
    def numIslands(self, grid: List[List[str]]) -> int:
        land = '1'
        water = '0'
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        count = 0

        def dfs(row, col):
            grid[row][col] = water
            for dr, dc in directions:
                mr = dr + row
                mc = dc + col
                if (mr < 0 or mc < 0 or mr >= rows or mc >= cols or grid[mr][mc] != land):
                    continue
                dfs(mr, mc)
                
        
        def bfs(row, col):
            pass

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land:
                    dfs(row, col)
                    count += 1
        
        return count




