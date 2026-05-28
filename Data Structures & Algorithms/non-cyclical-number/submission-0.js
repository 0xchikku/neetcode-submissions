class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    // Time - O(log n), Space - O(1)
    isHappy(n) {
        const unhappy = 4
        let cur = n
        while (cur !== 1) {
            let res = 0
            while (cur > 0) {
                let digit = (cur % 10)
                res += (digit * digit)
                cur = Math.floor(cur/10)
            }
            cur = res
            if (cur === unhappy) return false
        }
        return true
    }
}
