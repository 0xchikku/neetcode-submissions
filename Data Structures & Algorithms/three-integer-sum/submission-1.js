class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const res = []
        const n = nums.length
        if (n < 3) return res
        
        const sortedNums = nums.sort((a,b) => a-b)
        if (sortedNums[0] > 0) return res

        for (let i = 0; i < n - 2 && sortedNums[i] <= 0; i++) {
            if ( (i > 0) && (sortedNums[i] === sortedNums[i-1])) continue

            let left = i+1
            let right = n-1

            while (left < right) {
                const sum = sortedNums[i] + sortedNums[left] + sortedNums[right]

                if(sum > 0) right--
                else if (sum < 0) left++
                else {
                    res.push([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left++
                    right--
                    while (left < right && sortedNums[left] === sortedNums[left-1]) left++
                    while (left < right && sortedNums[right] === sortedNums[right+1]) right--
                }
            }

        }
        return res;
    }
}
