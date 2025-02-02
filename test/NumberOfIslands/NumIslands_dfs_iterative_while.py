# Iterative DFS solution using while loops

class Solution:
    def numIslands(grid):
        if not grid:
            return 0
        
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        i, j = 0, 0
        
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == '1':
                    num_islands += 1
                    stack = [(i, j)]
                    
                    while stack:
                        x, y = stack.pop()
                        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0':
                            continue
                        grid[x][y] = '0'
                        stack.append((x + 1, y))
                        stack.append((x - 1, y))
                        stack.append((x, y + 1))
                        stack.append((x, y - 1))
                j += 1
            i += 1
        
        return num_islands