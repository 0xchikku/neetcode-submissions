class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        // return this.recursive(n) // Time - O(2^n), Space - O(n)
        return this.topDown(n) // Time - O(n), Space - O(n)
    }

    // recursive(n) {
    //     if (n < 2) return 1
    //     return this.recursive(n-1) + this.recursive(n-2)
    // }

    topDown(n) {
        const cache = {}
        const ways = (n) => {
            if (n < 2) return 1
            if (n in cache) return cache[n]
            cache[n] = ways(n-1) + ways(n-2)
            return cache[n]
        }
        return ways(n)
    }
}
