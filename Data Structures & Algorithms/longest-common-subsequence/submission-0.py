class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        # time - O(2**(len1+len2)), space - O(len1+len2)
        def recursion(i, j):
            if i >= len1 or j >= len2:
                return 0

            if text1[i] == text2[j]:
                return 1 + recursion(i + 1, j + 1)
            else:
                case1 = recursion(i + 1, j)
                case2 = recursion(i, j + 2)
                return max(case1, case2)

        # return recursion(0, 0)

        # time - O(len1*len2), space - O(len1*len2)
        cache = [[None] * len2 for _ in range(len1)]

        def memoization(i, j):
            if i >= len1 or j >= len2:
                return 0
            if cache[i][j] is not None:
                return cache[i][j]

            if text1[i] == text2[j]:
                cache[i][j] = 1 + memoization(i + 1, j + 1)
            else:
                case1 = memoization(i + 1, j)
                case2 = memoization(i, j + 1)
                cache[i][j] = max(case1, case2)

            return cache[i][j]

        # return memoization(0,0)

        # time - O(len1*len2), space - O(len1*len2)
        def tabulation():
            dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
            for i in range(len1 - 1, -1, -1):
                for j in range(len2 - 1, -1, -1):
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            return dp[0][0]

        # return tabulation()

        # time - O(len1*len2), space - O(len2)
        def spaceOptimized():
            prevRow = [0] * (len2+1)
            for i in range(len1-1, -1, -1):
                curRow = [0]*(len2+1)
                for j in range(len2-1, -1, -1):
                    if text1[i] == text2[j]:
                        curRow[j] = 1 + prevRow[j+1]
                    else:
                        curRow[j] = max(curRow[j+1], prevRow[j])
                prevRow = curRow
            return prevRow[0]
        
        return spaceOptimized()

