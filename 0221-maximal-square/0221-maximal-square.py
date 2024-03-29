class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        
        dp=[[0]*(cols+1) for _ in range(rows+1)]
        square=0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]=="1":
                    dp[row+1][col+1]=min(dp[row][col+1],dp[row][col],dp[row+1][col])+1
                    square=max(dp[row+1][col+1],square)
        return square**2             