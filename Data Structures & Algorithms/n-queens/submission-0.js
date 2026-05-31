class Solution {
    /**
     * @param {number} n
     * @return {string[][]}
     */
    // time - O(n! + (S * n^2)), space - O(n^2)
    solveNQueens(n) {
        const res = []
        const QUEEN = "Q"
        const EMPTY = "."
        const colSet = new Set()
        const diagonalSet = new Set()
        const antiDiagonalSet = new Set()
        const board = Array.from({ length: n }, () => Array(n).fill(EMPTY))
        const recursion = (row) => {
            if (row === n) {
                const copy = []
                for (const r of board) {
                    copy.push(r.join(""))
                }
                res.push(copy)
                return
            }
            for (let col = 0; col < n; col++) {
                if ( colSet.has(col) || diagonalSet.has(row-col) || antiDiagonalSet.has(row+col)) continue

                board[row][col] = QUEEN
                colSet.add(col)
                diagonalSet.add(row-col)
                antiDiagonalSet.add(row+col)

                recursion(row+1)

                board[row][col] = EMPTY
                colSet.delete(col)
                diagonalSet.delete(row-col)
                antiDiagonalSet.delete(row+col)
            }
        }
        recursion(0)
        return res;
    }
}
