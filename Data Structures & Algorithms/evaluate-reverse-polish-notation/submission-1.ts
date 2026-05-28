class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    // Time - O(n), Space - (n)
    evalRPN(tokens: string[]): number {
        const operands = []
        const operators = {
            "+": (op1, op2) => op1 + op2,
            "-": (op1, op2) => op1 - op2,
            "*": (op1, op2) => op1 * op2,
            "/": (op1, op2) => Math.trunc(op1 / op2)
        };
        for (const token of tokens) {
            if (this.isOperand(token)) operands.push(Number(token))
            else {
                const [operand2, operand1] = [operands.pop(), operands.pop()]
                const res = operators[token](operand1, operand2)
                operands.push(res)
            }
        }
        return operands[0]
    }

    isOperand(token) {
        return !isNaN(Number(token))
    }
    
}
