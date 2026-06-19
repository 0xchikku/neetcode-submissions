class Solution:
    # time - O(n.m), space - O(n.m)
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        safe = set()
        queue = deque([])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for row in range(rows):
            if board[row][0] == "O" and (row, 0) not in safe:
                safe.add((row, 0))
                queue.append((row, 0))

            if board[row][cols - 1] == "O" and (row, cols - 1) not in safe:
                safe.add((row, cols - 1))
                queue.append((row, cols - 1))

        for col in range(cols):
            if board[0][col] == "O" and (0, col) not in safe:
                safe.add((0, col))
                queue.append((0, col))
            if board[rows - 1][col] == "O" and (rows - 1, col) not in safe:
                safe.add((rows - 1, col))
                queue.append((rows - 1, col))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                mr, mc = dr + row, dc + col
                if (
                    mr < 0
                    or mc < 0
                    or mr >= rows
                    or mc >= cols
                    or board[mr][mc] == "X"
                    or (mr, mc) in safe
                ):
                    continue
                safe.add((mr, mc))
                queue.append((mr, mc))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in safe:
                    board[row][col] = "X"
