class Solution:   
    def checkPartitioning(self, s: str) -> bool:
        
        dp = [[True for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

        for i in range(len(s)-2):
            for j in range(i+1,len(s)-1):
                if dp[0][i] and dp[i+1][j] and dp[j+1][len(s)-1]:
                    return True
       
        return False
        