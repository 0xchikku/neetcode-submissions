class Solution:
    # time - O(n.m), space - O(n.m)
    def numIslands(self, grid: List[List[str]]) -> int:
        water = '0'
        land = '1'
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        island = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == water:
                return
            
            grid[row][col] = water
            for [dr, dc] in directions:
                dfs(row+dr, col+dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land:
                    island += 1
                    dfs(row, col)

        return island