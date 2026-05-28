class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    // Time - O(log nm), Space - O(1)
    searchMatrix(matrix: number[][], target: number): boolean {
        if (!matrix || !matrix.length) return false
        const rowSize = matrix.length
        const colSize = matrix[0].length
        let left = 0
        let right = rowSize * colSize - 1
        while (left <= right) {
            const mid = left + Math.floor((right - left)/2)
            const i = Math.floor(mid / colSize);
            const j = mid % colSize
            if (matrix[i][j] < target) {
                left = mid + 1
            } else if (matrix[i][j] > target) {
                right = mid - 1
            } else {
                return true
            }
        }
        return false
    }
}
