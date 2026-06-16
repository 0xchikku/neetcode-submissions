from collections import deque
class Solution:
    # time - O(n.m), space - O(n.m)
    def numIslands(self, grid: List[List[str]]) -> int:
        water = "0"
        land = "1"
        rows, cols = len(grid), len(grid[0])
        visit = set()
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        count = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft() 
                for dr, dc in neighbours:
                    mr, mc = row + dr, col + dc
                    if (mr < 0 or mc < 0 or mr >= rows or mc >= cols or (mr, mc) in visit or grid[mr][mc] == water): 
                        continue
                    queue.append((mr, mc))
                    visit.add((mr, mc))

                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land and (row, col) not in visit:
                    count += 1
                    visit.add((row, col))
                    bfs(row, col)

        
        return count