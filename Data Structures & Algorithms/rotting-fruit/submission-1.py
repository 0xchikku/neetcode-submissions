class Solution:
    # time - O(n.m) space - O(n.m)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty = 0
        fresh = 1
        rotten = 2
        rows = len(grid)
        cols = len(grid[0])
        freshCount = 0
        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == fresh:
                    freshCount += 1
                elif grid[row][col] == rotten:
                    queue.append((row, col))
        
        minute = 0
        if freshCount == 0: return minute

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        while queue and freshCount > 0:
            level = len(queue)
            for _ in range(level):
                row, col = queue.popleft()
                for dr, dc in directions:
                    mr = dr + row
                    mc = dc + col
                    if mr < 0 or mc < 0 or mr >= rows or mc >= cols or grid[mr][mc] != fresh: 
                        continue
                    freshCount -= 1
                    grid[mr][mc] = rotten
                    queue.append((mr, mc))
            minute += 1
        
        return minute if freshCount == 0 else -1


