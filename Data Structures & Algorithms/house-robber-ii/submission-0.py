class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        # time - O(2**n), space - O(n)
        def recursion(index, length):
            if index >= length:
                return 0
            take = nums[index] + recursion(index + 2, length)
            skip = recursion(index + 1, length)
            return max(take, skip)

        # time - O(n), space - O(n)
        def memoization(index, length, cache):
            if index >= length:
                return 0
            if index in cache:
                return cache[index]
            take = nums[index] + memoization(index + 2, length, cache)
            skip = memoization(index + 1, length, cache)
            cache[index] = max(take, skip)
            return cache[index]

        # time - O(n), space - O(n)
        def tabulation(start, end):
            dp = [0] * (end + 3)
            for i in range(end, start - 1, -1):
                take = nums[i] + dp[i + 2]
                skip = dp[i + 1]
                dp[i] = max(take, skip)
            return dp[start]
        
        # time - O(n), space - O(1)
        def spaceOptimized(start, end):
            first = 0
            second = 0
            for i in range(end, start-1, -1):
                take = nums[i] + second
                skip = first
                first, second = max(take, skip), first
            return first
            
        def maxRob(length):
            case1 = spaceOptimized(0, length - 2)
            case2 = spaceOptimized(1, length - 1)
            return max(case1, case2)

        return maxRob(len(nums))
