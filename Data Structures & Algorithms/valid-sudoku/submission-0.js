class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const n = 9
        const skip = '.'
        const row = Array.from({ length: n }, () => new Set())
        const col = Array.from({ length: n }, () => new Set())
        const box = Array.from({ length: n }, () => new Set())

        for (let r = 0; r < n; r++) {
            for (let c = 0; c < n; c++) {
                const val = board[r][c];

                if (val === skip) continue

                const boxId = Math.floor(r/3) * 3 + Math.floor(c/3)
                if (row[r].has(val) || col[c].has(val) || box[boxId].has(val)) return false

                row[r].add(val)
                col[c].add(val)
                box[boxId].add(val)
            }
        }

        return true
    }
}
