class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const n = nums.length
        if (n < 2) return n;

        const uniqueNums = new Set(nums)
        let maxLen = 1

        for (let num of uniqueNums) {
            if ( uniqueNums.has(num-1) ) continue
            let count = 0
            while ( uniqueNums.has(num) ) {
                uniqueNums.delete(num)
                count += 1
                num += 1
            }
            maxLen = Math.max(maxLen, count)
        }
        return maxLen
    }
}
