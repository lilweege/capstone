# DFS Solution with direction vectors

class Solution:
    def numIslands(grid):
        if not grid:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark as visited
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands