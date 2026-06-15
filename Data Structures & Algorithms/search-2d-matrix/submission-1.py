class Solution:
    # time - O(log(m.n)), space - O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = (ROWS * COLS) - 1

        while left <= right:
            mid = left + (right-left)//2
            row = mid//COLS
            col = mid%COLS
            num = matrix[row][col]

            if num < target: left = mid + 1
            elif num > target: right = mid - 1
            else: return True
        
        return False
        