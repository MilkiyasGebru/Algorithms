class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @lru_cache(None)
        def dp(i,last_count,last_letter,k):
            
            count =0
            
            if last_count != 0:
                count = 1 if last_count == 1 else len(str(last_count)) + 1
                
            if k < 0:
                return inf
            
            if i == len(s): 
                return count
            
            if s[i] == last_letter:
                
                return min(
                    dp(i+1,last_count+1,last_letter,k)
                    ,dp(i+1,last_count,last_letter,k-1)
                )
            
            return min(
                dp(i+1,last_count,last_letter,k-1)
                ,dp(i+1,1,s[i],k) + count
            )
        
        return dp(0,0,"",k)
                
        

        
                
        
                        
            