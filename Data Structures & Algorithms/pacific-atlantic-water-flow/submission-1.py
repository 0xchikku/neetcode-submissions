class Solution:
    # time - O(rows * cols), space - O(rows * cols)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def bfs(visit, opposite = False):
            queue = deque([])
            for row in range(rows):
                if opposite:
                    cell = (row, cols-1)
                else:
                    cell = (row, 0)
                    
                if cell in visit:
                    continue
                else:
                    queue.append(cell)
                    visit.add(cell)
            
            for col in range(cols):
                if opposite:
                    cell = (rows-1, col)
                else:
                    cell = (0, col)

                if cell in visit:
                    continue
                else:
                    queue.append(cell)
                    visit.add(cell)
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    mr, mc = dr + row, dc + col
                    if mr < 0 or mc < 0 or mr == rows or mc == cols or (mr, mc) in visit or heights[mr][mc] < heights[row][col]:
                        continue
                    queue.append((mr, mc))
                    visit.add((mr, mc))
        
        bfs(pacific)
        bfs(atlantic, True)

        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                if cell in pacific and cell in atlantic:
                    res.append([row, col])
        
        return res
                
