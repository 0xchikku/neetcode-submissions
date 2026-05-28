class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    // time - o(), space - o()
    combinationSum(nums, target) {
        nums.sort((a,b) => a-b);
        const combinations = []
        const recursion = (index, sum, arr) => {
            if (sum === target) {
                combinations.push([...arr]);
                return
            }
            for (let i = index; i < nums.length; i++) {
                const newSum = nums[i] + sum;
                if (newSum > target) break;
                arr.push(nums[i])
                recursion(i, newSum, arr)
                arr.pop()
            }
        }
        recursion(0, 0, [])
        return combinations
    }
}
