class Solution:
    # time - O(n.m), space - O(n.m)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        water = -1
        treasure = 0
        land = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == treasure:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                mr, mc = dr + row, dc + col
                if mr < 0 or mc < 0 or mr >= rows or mc >= cols or grid[mr][mc] != land:
                    continue
                grid[mr][mc] = grid[row][col] + 1
                queue.append((mr, mc))
