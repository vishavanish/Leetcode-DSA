class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
       
        def dfs(row: int, col: int) -> int:
            
            island_sum = grid[row][col]
          
            grid[row][col] = 0
          
            for i in range(4):
                next_row = row + directions[i]
                next_col = col + directions[i + 1]
              
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    grid[next_row][next_col] != 0):
                    island_sum += dfs(next_row, next_col)
          
            return island_sum
      
        rows, cols = len(grid), len(grid[0])
      
        directions = [-1, 0, 1, 0, -1]
      
        island_count = 0
      
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    total_sum = dfs(i, j)
                    if total_sum % k == 0:
                        island_count += 1
      
        return island_count
