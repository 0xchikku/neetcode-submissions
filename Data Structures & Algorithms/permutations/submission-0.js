class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    // time - O(n * n!), space - O(n * n!)
    permute(nums) {
        const permutations = []
        const recursion = (path, used) => {
            if (path.length === nums.length) {
                permutations.push([...path])
                return
            }
            for (let i = 0; i < nums.length; i++) {
                if (used[i]) continue
                used[i] = true
                path.push(nums[i])
                recursion(path, used)
                path.pop()
                used[i] = false
            }
        }
        recursion([], {})
        return permutations;
    }
}
