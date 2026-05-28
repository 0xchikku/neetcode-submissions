class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const dp = [1, 1]
        let i = n - 2
        while ( i >= 0 ) {
            let temp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = temp
            i--
        }
        return dp[0]
    }
}
