class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost) {
        // return this.recursive(cost); // Time = O(2^n), Space = O(n)
        // return this.topDown(cost); // Time = O(n), Space = O(n)
        // return this.bottomUp(cost); // Time = O(n), Space = O(n)
        return this.optimizedBottomUp(cost); // Time = O(n), Space = O(1)
    }

    optimizedBottomUp(cost) {
        const n = cost.length;
        let prev1 = 0
        let prev2 = 0
        for (let i = n-1; i >= 0; i--) {
            const temp = prev2
            prev2 = cost[i] + Math.min(prev1, prev2)
            prev1 = temp
        }
        return Math.min(prev1, prev2)
    }

    bottomUp(cost) {
        const n = cost.length
        const dp = Array(n+2).fill(0)
        for (let i = n-1; i >= 0; i--) {
            dp[i] = cost[i] + Math.min(dp[i+1], dp[i+2])
        }
        return Math.min(dp[0], dp[1])
    }

    topDown(cost) {
        const n = cost.length;
        const cache = {}
        const calculateCost = (i) => {
            if (i >= n) return 0
            if (i in cache) return cache[i]
            cache[i] = cost[i] + Math.min(calculateCost(i+1), calculateCost(i+2));
            return cache[i]
        }
        return Math.min(calculateCost(0), calculateCost(1))
    }

    recursive(cost) {
        const n = cost.length
        const calculateCost = (i) => {
            if (i >= n) return 0
            return cost[i] + Math.min(calculateCost(i+1), calculateCost(i+2));
        }
        return Math.min(calculateCost(0), calculateCost(1))
    }
}
