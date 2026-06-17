class Solution:
    # time - O(n.m), space - O(n.m)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty = 0
        fresh = 1
        rotten = 2
        rows = len(grid)
        cols = len(grid[0])
        freshCount = 0
        queue = deque([])
        minute = 0
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if cell == rotten:
                    queue.append((row, col))
                elif cell == fresh:
                    freshCount += 1

        if freshCount == 0:
            return minute

        while queue and freshCount > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in direction:
                    mr, mc = dr + row, dc + col
                    if (
                        mr < 0
                        or mc < 0
                        or mr >= rows
                        or mc >= cols
                        or grid[mr][mc] == rotten
                        or grid[mr][mc] == empty
                    ):
                        continue
                    else:
                        grid[mr][mc] = rotten
                        freshCount -= 1
                        queue.append((mr, mc))
            minute += 1

        return minute if freshCount == 0 else -1
