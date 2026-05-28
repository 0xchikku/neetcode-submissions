class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const n = s.length
        if (n < 2) return true

        let left = 0
        let right = n-1

        while (left < right) {
            while (!this.isAlphaNumeric(s[left]) && left < right) left++
            while (!this.isAlphaNumeric(s[right]) && right > left) right--
            if (left >= right) break

            const isValid = s[left].toLowerCase() === s[right].toLowerCase()
            if (!isValid) return false
            left++
            right--
        }

        return true
    }

    isAlphaNumeric(char) {
        return (/^[a-z0-9]$/i).test(char)
    }
}
