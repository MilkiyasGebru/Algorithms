class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        dp = [1 for i in range(len(pairs))]
        
        
        for i in range(len(pairs)):
            
            for j in range(i):
                
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i],1+dp[j])
        
        return max(dp)
            