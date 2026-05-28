class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        return this.usingCompareArray(s1, s2);
    }

    // Time - O(n + m), Space - O(1)
    usingCompareArray(s1, s2) {
        if (s1.length > s2.length) return false

        // build frequency array for s1 and s2 for size len s1
        const s1Freq = Array(26).fill(0)
        const s2Freq = Array(26).fill(0)
        for (let i = 0; i < s1.length; i++) {
            s1Freq[this.findCharacterIndex(s1[i])] += 1
            s2Freq[this.findCharacterIndex(s2[i])] += 1
        }

        // compare freq of s1 and s2
        if(this.isSameArray(s1Freq, s2Freq)) return true

        // shift the window and compare to find the match
        let left = 0
        for (let right = s1.length; right < s2.length; right++) {
            
            // remove left
            const leftCharIndex = this.findCharacterIndex(s2[left])
            s2Freq[leftCharIndex] -= 1
            left++

            // add right
            const rightCharIndex = this.findCharacterIndex(s2[right])
            s2Freq[rightCharIndex] += 1

            // compare freq of s1 and s2
            if(this.isSameArray(s1Freq, s2Freq)) return true
        }

        // no match found
        return false
    }

    isSameArray(arr1, arr2) {
        for (let i = 0; i < 26; i++) {
            if (arr1[i] !== arr2[i]) return false
        }
        return true
    }

    findCharacterIndex(char) {
        return char.charCodeAt(0) - 'a'.charCodeAt(0)
    }
}
