class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0
        const n = prices.length
        if (n < 2) return maxProfit

        let buy = prices[0]
        for (const price of prices) {
            const profit = price - buy
            if (profit < 0) buy = price
            maxProfit = Math.max(maxProfit, profit)
        }
        return maxProfit
    }
}
