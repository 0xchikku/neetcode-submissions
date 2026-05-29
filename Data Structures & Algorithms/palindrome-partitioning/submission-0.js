class Solution {
    /**
     * @param {string} s
     * @return {string[][]}
     */
    // time - O(n × 2^n), space - O(n × 2^n)
    partition(s) {
        const res = []
        const path = []
        const recursion = (index) => {
            if (index === s.length) {
                res.push([...path])
                return
            }
            for (let i = index; i < s.length; i++) {
                if (!this.isPalindrome(s, index, i)) continue
                path.push(s.slice(index, i+1))
                recursion(i+1)
                path.pop()
            }
        }
        recursion(0)
        return res
    }

    isPalindrome(s, left, right) {
        while(left < right){
            if (s[left] !== s[right]) return false
            left++
            right--
        }
        return true
    }
}
