class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
    
        # time - O(2**n), space - O(n)
        def recursion(index):
            if index >= N:
                return 0
            take = nums[index] + recursion(index+2)
            skip = recursion(index+1)
            return max(take, skip)
        
        # time - O(n), space - O(n)
        def memoization(index, cache):
            if index >= N:
                return 0
            if index in cache:
                return cache[index]
            take = nums[index] + memoization(index+2, cache)
            skip = memoization(index+1, cache)
            cache[index] = max(take, skip)
            return cache[index]
        
        # time - O(n), space - O(n)
        def tabulation():
            dp = [0] * (N+2)
            for i in range(N-1, -1, -1):
                take = nums[i] + dp[i+2]
                skip = dp[i+1]
                dp[i] = max(take, skip)
            
            return dp[0]
        
        # time - O(n), space - O(1)
        def spaceOptimization():
            first = 0
            second = 0
            for i in range(N):
                first, second = second, max(nums[i]+first, second)
            return second

        return spaceOptimization()