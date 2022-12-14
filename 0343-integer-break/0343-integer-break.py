class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n)]
        answer = 1
        for i in range(3,n):
            for j in range(1,i):
                dp[i]=max(dp[i],dp[j]*dp[i-j])
        for i in range(1,n):
            answer = max(answer,dp[n-i]*dp[i])
        return answer