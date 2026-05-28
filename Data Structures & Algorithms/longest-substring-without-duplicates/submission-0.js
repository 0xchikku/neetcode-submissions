class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxLen = 0
        let left = 0
        const unique = new Set()

        for (let right = 0; right < s.length; right++) {
            while (unique.has(s[right])) {
                unique.delete(s[left])
                left++
            }
            unique.add(s[right])
            maxLen = Math.max(maxLen, right - left + 1)
        }

        return maxLen
    }
}
