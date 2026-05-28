class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const n = numbers.length
        let left = 0
        let right = n - 1

        while (left < right) {
            const sum = numbers[left] + numbers[right]
            if (sum === target) return [left+1, right+1]

            if(sum > target) right--
            else left++
        }

        return [-1, -1]
    }
}
