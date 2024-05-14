class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        ans1 = 0
        ans2 = 0
        row_mask = defaultdict(lambda: False)
        another_row_mask = defaultdict(lambda : False)
        # Just Flip the Rows  
        
        for col in range(len(grid[0])):
            zeros = 0
            another_zeros = 0
            for row in range(len(grid)):
                if col == 0:
                    row_mask[row] =  grid[row][col] == 0 
                    another_row_mask[row] = grid[row][col] == 1
                else:
                    zeros += 1 if( row_mask[row] == True and grid[row][col] == 1) or (grid[row][col]== 0 and row_mask[row] == False) else 0
                    another_zeros += 1 if( another_row_mask[row] == True and grid[row][col] == 1) or (grid[row][col]== 0 and another_row_mask[row] == False) else 0
            if col == 0:
                ans1 += len(grid)*(1 << (len(grid[0])-1))
                ans2 += len(grid)*(1 << (len(grid[0])-1))
            else:
                ones = len(grid) - zeros
                another_ones = len(grid) - another_zeros
                ans1 += max(ones,zeros)*(1<<(len(grid[0])-1-col))
                ans2 += max(another_ones,another_zeros)*(1<<(len(grid[0])-1-col))
                
        return max(ans1,ans2)