class Solution:
    # time - O(log n), space - O(1)
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        pn = abs(n)
        while pn:
            if pn & 1:
                ans = ans * x
            
            x = x * x
            pn = pn >> 1

        return ans if n >= 0 else (1 / ans)