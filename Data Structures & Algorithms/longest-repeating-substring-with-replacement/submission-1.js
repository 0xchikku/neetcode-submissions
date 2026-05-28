class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    // Time - O(n), Space - O(1)
    characterReplacement(s, k) {
        const freq = Array(26).fill(0)
        let maxFreq = 0
        let maxLen = 0
        let left = 0
        for (let right = 0; right < s.length; right++) {
            const index = s[right].charCodeAt(0) - 'A'.charCodeAt(0)
            freq[index] += 1
            maxFreq = Math.max(maxFreq, freq[index])
            if (((right - left + 1) - maxFreq) > k) {
                const index = s[left].charCodeAt(0) - 'A'.charCodeAt(0)
                freq[index] -= 1
                left += 1
            }
            maxLen = Math.max(maxLen, right - left + 1)
        }
        return maxLen
    }
}
