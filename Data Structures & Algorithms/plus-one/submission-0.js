class Solution {
    /**
     * @param {number[]} digits
     * @return {number[]}
     */
    // Time - O(n), Space - O(1)
    plusOne(digits) {
        const len = digits.length
        for (let i = len-1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++
                return digits
            } 
            digits[i] = 0
        }
        digits.unshift(1)
        return digits
    }
}
