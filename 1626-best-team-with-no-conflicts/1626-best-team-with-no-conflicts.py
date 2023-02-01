class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        new_array=[]
        
        for index in range(len(scores)):
            
            new_array.append((ages[index],scores[index]))
        
        new_array.sort()
        

        dp = [[0 for _ in range(len(scores))] for _ in range(len(scores))]
        
        for i in range(len(scores)):
            
            if new_array[-1][1] >= new_array[i][1]:
                
                dp[-1][i] = new_array[-1][1] 
            
        
        for index in range(len(scores)-2,-1,-1):
            
            for prevIndex in range(len(scores)):
                
                if new_array[index][1] >= new_array[prevIndex][1]:
                    
                    dp[index][prevIndex] = max(new_array[index][1] + dp[index+1][index],dp[index+1][prevIndex])
                    
                else:
                    
                    dp[index][prevIndex] = dp[index+1][prevIndex]
                    
        return max(dp[0])
                
        
        
        
        
            
            
            
           