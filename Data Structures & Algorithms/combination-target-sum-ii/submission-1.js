class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    // time - O(n * 2^n), space - O(2^n)
    combinationSum2(candidates, target) {
        candidates.sort((a,b) => a-b);
        const combinations = [];
        const recursion = (index, remaining, nums) => {
            if (remaining === 0) {
                combinations.push([...nums])
                return
            }
            if (index === candidates.length || remaining < 0) return
            const num = candidates[index]
            nums.push(num)
            recursion(index+1, remaining-num, nums)
            nums.pop()
            while (index < candidates.length && candidates[index] === candidates[index+1]) {
                index++
            }
            recursion(index+1, remaining, nums)
        }
        recursion(0, target, [])
        return combinations
    }
}
