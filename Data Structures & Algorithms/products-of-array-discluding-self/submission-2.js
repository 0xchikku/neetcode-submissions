class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length
        const ans = new Array(n).fill(1)

        let left = 1
        for (let i = 0; i < n; i++) {
            ans[i] = left
            left *= nums[i]
        }

        let right = 1
        for (let i = n-1; i >= 0; i--) {
            ans[i] *= right
            right *= nums[i]
        }
        
        return ans
    }
}
