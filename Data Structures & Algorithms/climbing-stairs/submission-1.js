class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const cache = []
        const dfs = (n) => {
            if ( n <= 0 ) return n === 0
            if ( cache[n] > 0 ) return cache[n]
            cache[n] = dfs(n-1) + dfs(n-2)
            return cache[n]
        }
        return dfs(n)
    }
}
