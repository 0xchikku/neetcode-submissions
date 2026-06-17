class Solution:
    # time - O(n.m), space - O(n.m)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        land = 1
        water = 0
        maxArea = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(row, col):
            area = 0
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                area += 1
                for dr, dc in directions:
                    mr, mc = row + dr, col + dc
                    if (mr < 0 or mc < 0 or mr >= rows or mc >= cols or grid[mr][mc] == water or (mr, mc) in visit):
                        continue
                    queue.append((mr, mc))
                    visit.add((mr, mc))

            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land and (row, col) not in visit:
                    visit.add((row, col))
                    maxArea = max(maxArea, bfs(row, col))
        
        return maxArea

