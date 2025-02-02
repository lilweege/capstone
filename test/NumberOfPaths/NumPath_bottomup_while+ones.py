# Bottom up solution initliazed with 1's instead of 0's, and uses while loops

class Solution:
    def uniquePaths(m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        i = 1
        while i < m:
            j = 1
            while j < n:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                j += 1
            i += 1
        
        return dp[m - 1][n - 1]