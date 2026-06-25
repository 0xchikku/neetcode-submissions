class Solution:
    # time - O(n.m), space - O(n.m)
    def solve(self, board: List[List[str]]) -> None:
        way = 'O'
        close = 'X'
        visited = 'V'
        rows = len(board)
        cols = len(board[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]


        def dfs(row, col):
            if board[row][col] != way: return
            board[row][col] = visited
            for dr, dc in directions:
                mr = dr + row
                mc = dc + col
                if mr < 0 or mc < 0 or mr >= rows or mc >= cols or board[mr][mc] != way:
                    continue
                dfs(mr, mc)
        
        def bfs(row, col):
            pass

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == visited:
                    board[row][col] = way
                elif board[row][col] == way:
                    board[row][col] = close

