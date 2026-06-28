class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        startRow = 0
        startCol = 0
        rows = m
        cols = n

        # time - O(2**(rows+cols)), space - O(rows+cols)
        def recursion(row, col):
            if row >= rows or col >= cols:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1

            return recursion(row + 1, col) + recursion(row, col + 1)
        
        # time - O(rows*cols), space - O(rows*cols)
        cache = [[0] * cols for _ in range(rows)]
        def memoization(row, col):
            if row >= rows or col >= cols:
                return 0
            if row == rows-1 and col == cols-1:
                return 1
            if cache[row][col] > 0:
                return cache[row][col]
            
            cache[row][col] = memoization(row+1, col) + memoization(row, col+1)
            return cache[row][col]
        
        # return memoization(startRow, startCol)
        
        # time - O(rows*cols), space - O(cols)
        def spaceOptimized():
            prevRow = [0] * cols
            for row in range(rows-1, -1, -1):
                curRow = [0] * cols
                curRow[cols-1] = 1
                for col in range(cols-2, -1, -1):
                    curRow[col] = curRow[col+1] + prevRow[col]
                prevRow = curRow
            return prevRow[0]
        
        return spaceOptimized()

        
