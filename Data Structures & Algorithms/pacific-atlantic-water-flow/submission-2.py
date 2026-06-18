class Solution:
    # time - O(rows * cols), space - O(rows * cols)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pacific, atlantic = set(), set()
        res = []

        def dfs(row, col, visit):
            if (row, col) in visit:
                return
            visit.add((row, col))
            for dr, dc in directions:
                mr, mc = dr + row, dc + col
                if (
                    mr < 0
                    or mc < 0
                    or mr == rows
                    or mc == cols
                    or heights[mr][mc] < heights[row][col]
                    or (mr, mc) in visit
                ):
                    continue
                dfs(mr, mc, visit)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                if cell in pacific and cell in atlantic:
                    res.append([row, col])

        return res
