class Solution:
    # time - O(n.m), space - O(n.m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        pacific = set()
        atlantic = set()

        def bfs(cell, visit):
            row, col = cell
            visit.add((row, col))
            queue = deque([(row, col)])

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    mr = dr + row
                    mc = dc + col
                    if mr < 0 or mc < 0 or mr >= rows or mc >= cols or heights[mr][mc] < heights[row][col] or (mr, mc) in visit:
                        continue
                    visit.add((mr, mc))
                    queue.append((mr, mc))

        def dfs(cell, visit):
            row, col = cell
            if cell in visit:
                return 
            visit.add(cell)
            for dr, dc in directions:
                mr = dr + row
                mc = dc + col
                if mr < 0 or mc < 0 or mr >= rows or mc >= cols or heights[mr][mc] < heights[row][col] or (mr, mc) in visit:
                    continue
                dfs((mr, mc), visit)

        for row in range(rows):
            bfs((row, 0), pacific)
            bfs((row, cols-1), atlantic)
        
        for col in range(cols):
            bfs((0, col), pacific)
            bfs((rows-1, col), atlantic)

        res = []
        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                if cell in pacific and cell in atlantic:
                    res.append([row, col])
        
        return res