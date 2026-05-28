class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const trackOpenBrackets = []
        const closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for (const bracket of s) {
            const isOpenBracket = !closeToOpen[bracket]
            if (isOpenBracket) trackOpenBrackets.push(bracket)
            else {
                const len = trackOpenBrackets.length
                if (!len || closeToOpen[bracket] !== trackOpenBrackets[len-1]) return false
                trackOpenBrackets.pop()
            }
        }

        return !trackOpenBrackets.length
    }
}
