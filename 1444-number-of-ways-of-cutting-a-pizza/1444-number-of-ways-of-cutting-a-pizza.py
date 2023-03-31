class Solution:
    def calculate(self,topRow,topCol,bottomRow,bottomCol,prefix):
        
        
        return self.isValid(bottomRow,bottomCol,prefix) - self.isValid(bottomRow,topCol-1,prefix) - self.isValid(topRow-1,bottomCol,prefix) + self.isValid(topRow-1,topCol-1,prefix)
    
    def isValid(self,row,col,dp):
        # print(row,col)
        if 0 <= row < len(dp) and 0 <= col < len(dp[0]):
            return dp[row][col]
        
        return 0
    
    def calculate_prefix(self,pizza):
        
        prefix = [[0 for _ in range(len(pizza[0]))] for _ in range(len(pizza))]
        
        for row in range(len(pizza)):
            for col in range(len(pizza[0])):
                
                prefix[row][col] += self.isValid(row-1,col,prefix) + self.isValid(row,col-1,prefix) - self.isValid(row-1,col-1,prefix) + (1 if pizza[row][col] == "A" else 0)
                
        return prefix
    
    def ways(self, pizza: List[str], k: int) -> int:
        
        prefix = self.calculate_prefix(pizza)
        mod = 10**9 + 7
        m,n = len(pizza)-1,len(pizza[0])-1
        
        @lru_cache(None)
        def dp(topRow,topCol,k):
            val = self.calculate(topRow,topCol,m,n,prefix)
            if val < k:
                return 0
            
            if k == 1:
                return 1
            
            ans = 0
            # Horizontal Cuts
            for i in range(topRow,m):
                    if self.calculate(topRow,topCol,i,n,prefix) > 0:
                        ans += dp(i+1,topCol,k-1)
                
            # Vertical Cuts
            for i in range(topCol,n):
                if self.calculate(topRow,topCol,m,i,prefix) > 0:
                    ans += dp(topRow,i+1,k-1)
                
            return ans
        
        return dp(0,0,k)%mod

        