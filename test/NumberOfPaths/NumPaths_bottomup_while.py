# Bottom up DP using while loops

class Solution:
    def uniquePaths(m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        i = 0
        while i < m:
            dp[i][0] = 1
            i += 1
        
        j = 0
        while j < n:
            dp[0][j] = 1
            j += 1
        
        i = 1
        while i < m:
            j = 1
            while j < n:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                j += 1
            i += 1
        
        return dp[m - 1][n - 1]