class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        return nums.reduce((prev, cur) => prev ^ cur)
    }
}
