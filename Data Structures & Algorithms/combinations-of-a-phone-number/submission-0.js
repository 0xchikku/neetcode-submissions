class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    // time - O(n * 4^n), space - O(n * 4^n)
    letterCombinations(digits) {
        const res = []
        if (digits.length === 0) return res
        const digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqsr",
            "8": "tuv",
            "9": "wxyz",
        };
        
        const recursion = (index, str) => {
            if (str.length === digits.length) {
                res.push(str)
                return
            }
            for (const letter of digitToLetters[digits[index]]) {
                recursion(index+1, str + letter)
            }
        }
        recursion(0, "")
        return res
    }
}
