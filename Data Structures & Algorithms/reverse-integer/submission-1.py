class Solution:
    def reverse(self, x: int) -> int:
        INT32_MAX = 2147483647
        INT32_MIN = -2147483648
        INT32_MAX_WITHOUT_LAST_DIGIT = math.trunc(INT32_MAX / 10)
        INT32_MAX_LAST_DIGIT = INT32_MAX % 10
        INT32_MIN_WITHOUT_LAST_DIGIT = math.trunc(INT32_MIN / 10)
        INT32_MIN_LAST_DIGIT = int(math.fmod(INT32_MIN, 10))

        res = 0

        while x != 0:
            lastDigit = int(math.fmod(x, 10))
            x = math.trunc(x / 10)

            # out of bound
            if (
                res > INT32_MAX_WITHOUT_LAST_DIGIT
                or (res == INT32_MAX_WITHOUT_LAST_DIGIT and lastDigit > INT32_MAX_LAST_DIGIT)
                or (
                    res < INT32_MIN_WITHOUT_LAST_DIGIT
                    or (res == INT32_MIN_WITHOUT_LAST_DIGIT and lastDigit > INT32_MIN_LAST_DIGIT)
                )
            ):
                return 0
            
            res = (res * 10) + lastDigit
        
        return res
