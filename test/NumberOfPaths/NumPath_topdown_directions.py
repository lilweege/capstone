# DFS solution with hard coded memoization and direction vectors

class Solution:
    def uniquePaths(m: int, n: int) -> int:
        memo = {}
        directions = [(1, 0), (0, 1)]
        
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            total = 0
            for dx, dy in directions:
                total += dfs(i + dx, j + dy)
            memo[(i, j)] = total
            return memo[(i, j)]
        
        return dfs(0, 0)