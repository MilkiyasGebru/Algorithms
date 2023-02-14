class Solution:
    def minimumDeletions(self, s: str) -> int:
        
    
        dp = [[0 for _ in range(2)] for _ in range(len(s) + 1)]
        letter = ["a","b"]
        
        for i in range(len(s)-1,-1,-1):
            
            for j in range(2):
                
                if letter[j] == "b":
                    
                    dp[i][j] = ( 1 + dp[i+1][1] ) if letter[j] != s[i] else dp[i+1][j]
                    
                else:
                    
                    dp[i][j] = min((s[i] != letter[j]) + dp[i+1][j],dp[i+1][1])
                    
        return dp[0][0]
            
            