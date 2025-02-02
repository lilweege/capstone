# Iterative DP done in reverse order
class Solution:
    def uniquePaths(m: int, n: int) -> int:
        dp = [1] * n
        
        i = m - 2
        while i >= 0:
            j = n - 2
            while j >= 0:
                dp[j] += dp[j + 1]
                j -= 1
            i -= 1
        
        return dp[0]