class Solution {
    /**
     * @param {character[][]} board
     * @param {string} word
     * @return {boolean}
     */
    exist(board, word) {
        const ROWS = board.length;
        const COLS = board[0].length;
        
        const isMatch = (row, col, index) => {
            if (index === word.length) return true
            if (
                row < 0 ||
                col < 0 ||
                row === ROWS ||
                col === COLS ||
                board[row][col] !== word[index] ||
                board[row][col] === null
            ) return false
            const letter = board[row][col]
            board[row][col] = null
            const res = (
                isMatch(row+1, col, index+1) ||
                isMatch(row-1, col, index+1) ||
                isMatch(row, col+1, index+1) ||
                isMatch(row, col-1, index+1)
            )
            board[row][col] = letter
            return res;
        }

        for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
                if (board[row][col] !== word[0]) continue
                if (isMatch(row, col, 0)) return true
            }
        }
        return false
    }
}
