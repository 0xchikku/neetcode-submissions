class Solution:
    # time - O(n.m), space - O(n.m)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image

        original_color = image[sr][sc]
        ROWS = len(image)
        COLS = len(image[0])

        def dfs(row, col):
            if ( row < 0 or 
            col < 0 or 
            row == ROWS or 
            col == COLS or 
            image[row][col] != original_color): 
                return
            
            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        dfs(sr, sc)
        return image
