class Solution {
    /**
     * @param {number[][]} matrix
     * @return {number[]}
     */
    // time - O(row * col), space - O(row * col)
    spiralOrder(matrix) {
        const lenRow = matrix.length;
        const lenCol = matrix[0].length;
        const output = [];
        let left = 0;
        let top = 0;
        let right = lenCol - 1;
        let bottom = lenRow - 1;
        while (left <= right && top <= bottom) {
            for (let i = left; i <= right; i++) {
                output.push(matrix[top][i]);
            }
            top++;

            if (top > bottom) break;
            for (let i = top; i <= bottom; i++) {
                output.push(matrix[i][right]);
            }
            right--;

            if (left > right) break;
            for (let i = right; i >= left; i--) {
                output.push(matrix[bottom][i]);
            }
            bottom--;

            for (let i = bottom; i >= top; i--) {
                output.push(matrix[i][left]);
            }
            left++;
        }
        return output;
    }
}
