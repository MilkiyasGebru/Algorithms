class Solution:
    def checkRecord(self, n: int) -> int:
        
        dp = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
        
        
        for i in range(n,-1,-1):
            for j in range(3,-1,-1):
                for k in range(2,-1,-1):
                    if j > 1:
                        continue
                    if i == n:
                        dp[i][j][k] = 1
                    else:
                        dp[i][j][k] = dp[i+1][j+1][0] + dp[i+1][j][0] + dp[i+1][j][k+1]
                        dp[i][j][k] %= (10**9 + 7)
        return dp[0][0][0]