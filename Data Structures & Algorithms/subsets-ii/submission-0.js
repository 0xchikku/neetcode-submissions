class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        const subsets = []
        nums.sort((a,b) => a-b)
        const recursion = (index, subset) => {
            subsets.push([...subset])
            for (let i = index; i < nums.length; i++) {
                if (i > index && nums[i] === nums[i-1]) continue
                subset.push(nums[i])
                recursion(i+1, subset)
                subset.pop()
            }
        }
        recursion(0, [])
        return subsets
    }
}
