class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.recursion(n)
        # return self.memoization(n, {})
        # return self.tabulation(n)
        return self.spaceOptimized(n)

    # time - O(2^n), space - O(n)
    def recursion(self, n):
        if n < 3:
            return n
        return self.recursion(n-1) + self.recursion(n-2)
    
    # time - O(n), space - O(n)
    def memoization(self, n, cache):
        if n < 3:
            return n
        if n in cache:
            return cache[n]
        
        cache[n] = self.memoization(n-1, cache) + self.memoization(n-2, cache)
        return cache[n]
    
    # time - O(n), space - O(n)
    def tabulation(self, n):
        if n < 3:
            return n

        cache = [0] * (n+1)
        cache[1] = 1
        cache[2] = 2

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]
    
    # time - O(n), space - O(1)
    def spaceOptimized(self, n):
        if n < 3:
            return n
        
        num1 = 1
        num2 = 2

        for _ in range(3, n+1):
            temp = num2
            num2 = num1 + num2
            num1 = temp
        
        return num2