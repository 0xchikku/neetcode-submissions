class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    // Time - O(n), Space - O(n)
    countBits(n) {
        const ans = Array(n+1).fill(0)
        for (let i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1)
        }
        return ans
    }
}
