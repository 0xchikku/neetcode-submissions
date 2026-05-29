class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    // time - O(Catalan number * n), space - O(Catalan number * n)
    generateParenthesis(n) {
        const stack = []
        const res = []
        const recursion = (openUsed, closeUsed) => {
            if (openUsed === n && closeUsed === n) {
                res.push(stack.join(""))
                return
            }
            if (openUsed < n) {
                stack.push("(")
                recursion(openUsed+1, closeUsed)
                stack.pop()
            }
            if (closeUsed < openUsed) {
                stack.push(")")
                recursion(openUsed, closeUsed+1)
                stack.pop()
            }
        }
        recursion(0, 0)
        return res
    }
}
