class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        mod = 10**9 + 7
        @cache
        def dp(row,col,move):
            
            if row < 0 or row == m or col < 0 or col == n:
                return 1
            
            if move == 0:
                return 0
            
            return (dp(row+1,col,move-1) + dp(row-1,col,move-1) + dp(row,col+1,move-1)+dp(row,col-1,move-1))%mod
        
        return dp(startRow,startColumn,maxMove)