class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    setZeroes(matrix) {
        const lenRow = matrix.length;
        const lenCol = matrix[0].length;
        let isFirstRowZero = false;
        let isFirstColZero = false;

        for (let col = 0; col < lenCol; col++) {
            if (matrix[0][col] === 0) {
                isFirstRowZero = true;
                break;
            }
        }
        for (let row = 0; row < lenRow; row++) {
            if (matrix[row][0] === 0) {
                isFirstColZero = true;
                break;
            }
        }
        for (let row = 1; row < lenRow; row++) {
            for (let col = 1; col < lenCol; col++) {
                if (matrix[row][col] === 0) {
                    matrix[0][col] = 0;
                    matrix[row][0] = 0;
                }
            }
        }
        for (let row = 1; row < lenRow; row++) {
            for (let col = 1; col < lenCol; col++) {
                if (matrix[0][col] === 0 || matrix[row][0] === 0) matrix[row][col] = 0;
            }
        }
        if (isFirstRowZero) {
            for (let col = 0; col < lenCol; col++) {
                matrix[0][col] = 0;
            }
        }
        if (isFirstColZero) {
            for (let row = 0; row < lenRow; row++) {
                matrix[row][0] = 0;
            }
        }
    }
}
