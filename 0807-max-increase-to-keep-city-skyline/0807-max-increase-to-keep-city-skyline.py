class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        horizontal = defaultdict(int)
        vertical = defaultdict(int)
        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                horizontal[row] = max(horizontal[row],grid[row][col])
                vertical[col] = max(vertical[col],grid[row][col])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                answer += min(vertical[col],horizontal[row]) - grid[row][col]
        
        return answer