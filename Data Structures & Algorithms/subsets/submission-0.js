class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    // time - O(n * 2^n), space - O(n * 2^n)
    subsets(nums) {
        const res = [];
        const recursion = (index, subset) => {
            if (index === nums.length) {
                res.push([...subset]);
                return;
            }
            subset.push(nums[index]);
            recursion(index + 1, subset)
            subset.pop();
            recursion(index + 1, subset)
        }
        recursion(0, [])
        return res;
    }
}
