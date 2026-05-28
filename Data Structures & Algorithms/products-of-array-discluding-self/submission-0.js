class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const prefix = []
        const suffix = []
        const n = nums.length

        let left = 1;
        for (let i = 0; i < n; i++) {
            prefix[i] = left
            left *= nums[i]
        }
        
        let right = 1;
        for (let i = n-1; i >= 0; i--) {
            suffix[i] = right
            right *= nums[i]
        }

        const output = []
        for (let i = 0; i < n; i++) {
            output.push(prefix[i] * suffix[i])
        }
        return output
    }
}
