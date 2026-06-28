class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        space = 0
        obstacle = 1

        if obstacleGrid[0][0] == obstacle or obstacleGrid[rows - 1][cols - 1] == obstacle:
            return 0

        # time - O(2**(rows+cols)), space - O(rows+cols)
        def recursion(row, col):
            if row >= rows or col >= cols or obstacleGrid[row][col] == obstacle:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1

            return recursion(row + 1, col) + recursion(row, col + 1)

        # return recursion(0,0)

        # time - O(rows*cols), space - O(rows*cols)
        cache = [[None] * cols for _ in range(rows)]

        def memoization(row, col):
            if row >= rows or col >= cols or obstacleGrid[row][col] == obstacle:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1
            if cache[row][col] is not None:
                return cache[row][col]

            right = memoization(row, col + 1)
            down = memoization(row + 1, col)
            cache[row][col] = right + down
            return cache[row][col]

        # return memoization(0, 0)

        # time - O(rows * cols), space - O(rows * cols)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        def tabulation():
            dp[rows - 1][cols - 1] = 1
            for row in range(rows - 1, -1, -1):
                for col in range(cols - 1, -1, -1):
                    if (row == rows - 1 and col == cols - 1) or obstacleGrid[row][col] == obstacle:
                        continue
                    dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
            return dp[0][0]

        # return tabulation()

        # time - O(rows*cols), space - O(cols)
        def spaceOptimized():
            prevRow = [0] * cols
            for row in range(rows - 1, -1, -1):
                curRow = [0] * (cols + 1)
                if row == rows - 1:
                    curRow[cols - 1] = 1
                for col in range(cols - 1, -1, -1):
                    if obstacleGrid[row][col] == obstacle or (row == rows - 1 and col == cols - 1):
                        continue
                    curRow[col] = curRow[col + 1] + prevRow[col]
                prevRow = curRow
            return prevRow[0]

        return spaceOptimized()
