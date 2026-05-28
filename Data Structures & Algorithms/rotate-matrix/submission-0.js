class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    rotate(matrix) {
        const len = matrix.length;
        // transpose of a matrix, converting row to column
        for (let row = 0; row < len; row++) {
            for (let col = row+1; col < len; col++) {
                [matrix[row][col], matrix[col][row]] = [matrix[col][row], matrix[row][col]];
            }
        }
        // reverse each row
        for (let row = 0; row < len; row++) {
            let left = 0;
            let right = len - 1;
            while (left < right) {
                [matrix[row][left], matrix[row][right]] = [matrix[row][right], matrix[row][left]];
                left++
                right--
            }
        }
    }
}
