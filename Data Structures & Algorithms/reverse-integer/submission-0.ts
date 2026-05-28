class Solution {
    /**
     * @param {number} x
     * @return {number}
     */
    reverse(x: number): number {
        const INT32_MAX = 2147483647;
        const INT32_MIN = -2147483648;
        const INT32_MAX_LAST_DIGIT = INT32_MAX % 10
        const INT32_MAX_WITHOUT_LAST_DIGIT = Math.trunc(INT32_MAX / 10)
        const INT32_MIN_LAST_DIGIT = INT32_MIN % 10
        const INT32_MIN_WITHOUT_LAST_DIGIT = Math.trunc(INT32_MIN / 10)

        let res = 0
        while (x !== 0) {
            const lastDigit = x % 10
            x = Math.trunc(x/10)

            const isOutOfBound = (
                ( (res > INT32_MAX_WITHOUT_LAST_DIGIT) || (res === INT32_MAX_WITHOUT_LAST_DIGIT && lastDigit > INT32_MAX_LAST_DIGIT) )
                || ( (res < INT32_MIN_WITHOUT_LAST_DIGIT) || (res === INT32_MIN_WITHOUT_LAST_DIGIT && lastDigit < INT32_MIN_LAST_DIGIT) )
            )
            if (isOutOfBound) return 0

            res = res * 10 + lastDigit
        }
        return res
    }
}
