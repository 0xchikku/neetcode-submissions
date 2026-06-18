class Solution:
    # time - O(rows * cols), space - O(rows * cols)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(starts):
            queue = deque(starts)
            visit = set(starts)

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    mr, mc = dr + row, dc + col
                    if (
                        mr < 0
                        or mc < 0
                        or mr == rows
                        or mc == cols
                        or (mr, mc) in visit
                        or heights[mr][mc] < heights[row][col]
                    ):
                        continue
                    queue.append((mr, mc))
                    visit.add((mr, mc))
            
            return visit

        pacificStarts = set()
        atlanticStarts = set()
        for row in range(rows):
            pacificStarts.add((row, 0))
            atlanticStarts.add((row, cols - 1))
        
        for col in range(cols):
            pacificStarts.add((0, col))
            atlanticStarts.add((rows-1,col))

        pacific = bfs(pacificStarts)
        atlantic = bfs(atlanticStarts)

        res = []
        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                if cell in pacific and cell in atlantic:
                    res.append([row, col])

        return res
