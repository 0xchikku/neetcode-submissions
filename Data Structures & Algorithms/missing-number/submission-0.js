class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    // Time - O(n), Space - O(1)
    missingNumber(nums) {
        let missing = nums.length
        for (let i = 0; i < nums.length; i++) {
            missing ^= (i ^ nums[i])
        }
        return missing
    }
}
