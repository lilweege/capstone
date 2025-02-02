# Iterative DFS solutions

class Solution:
    def num_islands_dfs_stack(grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    stack = [(r, c)]
                    while stack:
                        row, col = stack.pop()
                        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1':
                            grid[row][col] = '0'
                            stack.extend([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)])
                    islands += 1
        
        return islands