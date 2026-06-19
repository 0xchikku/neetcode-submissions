class Solution:
    # time - O(n.m), space - O(n.m)
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(row, col):
            for dr, dc in directions:
                mr, mc = row + dr, col + dc
                if mr < 0 or mc < 0 or mr >= rows or mc >= cols or board[mr][mc] != "O":
                    continue
                board[mr][mc] = "S"
                dfs(mr, mc)

        for row in range(rows):
            if board[row][0] == "O":
                board[row][0] = "S"
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                board[row][cols - 1] = "S"
                dfs(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == 'O':
                board[0][col] = 'S'
                dfs(0, col)
            if board[rows-1][col] == 'O':
                board[rows-1][col] = 'S'
                dfs(rows-1, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'
