class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {

        const dfs = (n) => {
            if ( n <= 0 ) return n === 0
            return dfs(n-1) + dfs(n-2)
        }
        return dfs(n)
    }
}
