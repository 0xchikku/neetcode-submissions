class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    // time - O(n!), space - O(n)
    totalNQueens(n) {
        let count = 0
        const column = new Set()
        const diagonal = new Set()
        const antiDiagonal = new Set()
        const recursion = (row) => {
            if (row === n) {
                count++
                return
            }
            for (let col = 0; col < n; col++) {
                if (column.has(col) || diagonal.has(row-col) || antiDiagonal.has(row+col)) continue

                column.add(col)
                diagonal.add(row-col)
                antiDiagonal.add(row+col)

                recursion(row+1)

                column.delete(col)
                diagonal.delete(row-col)
                antiDiagonal.delete(row+col)
            }
        }
        recursion(0)
        return count
    }
}
