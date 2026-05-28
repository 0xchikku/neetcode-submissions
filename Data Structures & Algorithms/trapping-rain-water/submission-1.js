class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const n = height.length
        if (n < 3) return 0

        let left = 0
        let right = n-1
        let leftMax = height[left]
        let rightMax = height[right]
        let water = 0

        while (left < right) {
        let waterHere = 0
            if (leftMax < rightMax) {
                left++
                leftMax = Math.max(leftMax, height[left])
                waterHere = leftMax - height[left]
            } else {
                right--
                rightMax = Math.max(rightMax, height[right])
                waterHere = rightMax - height[right]
            }
            water += waterHere
        }

        return water
    }
}
