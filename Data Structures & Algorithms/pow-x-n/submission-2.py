class Solution:
    # time - O(log n), space - O(1)
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        base = x
        exp = abs(n)

        while exp:
            if exp & 1:
                ans *= base

            base *= base
            exp >>= 1

        return ans if n >= 0 else (1 / ans)
