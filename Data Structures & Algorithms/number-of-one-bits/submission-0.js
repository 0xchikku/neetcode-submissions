class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
        // return this.solution0(n)
        return this.solution1(n)
    }

    solution1 (n) {
        let count = 0
        while (n > 0) {
            count += 1
            n = n & (n-1)
        }
        return count
    }

    solution0 (n) {
        let count = 0
        while (n > 0) {
            count += (n & 1)
            n = n >>> 1
        }
        return count
    }
}
