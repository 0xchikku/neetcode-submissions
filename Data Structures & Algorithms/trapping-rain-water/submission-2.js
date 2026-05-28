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
        let leftMax = 0
        let rightMax = 0
        let water = 0

        while (left < right) {
        let waterHere = 0
            if (height[left] < height[right]) {
                if (height[left] > leftMax) leftMax = height[left]
                else waterHere = leftMax - height[left]
                left++
            } else {
                if (height[right] > rightMax) rightMax = height[right]
                else waterHere = rightMax - height[right]
                right--
            }
            water += waterHere
        }

        return water
    }
}
