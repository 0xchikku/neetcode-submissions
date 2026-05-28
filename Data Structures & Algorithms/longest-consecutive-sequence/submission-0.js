class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const n = nums.length
        if (n < 2) return n

        const numsSet = new Set(nums)
        const startingPoints = []
        let maxLen = 1

        for (const num of nums) {
            if ( numsSet.has(num-1) ) continue
            startingPoints.push(num)
        }

        for (let start of startingPoints) {
            let count = 0
            while ( numsSet.has(start) ) {
                start += 1
                count += 1
            }
            maxLen = Math.max(count, maxLen)
        }

        return maxLen
    }
}
