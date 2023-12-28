class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        
        @cache
        def dp(index,last_character,count,k):
            
            
            if k < 0:
                return math.inf
            
            if index == len(s):
                if last_character == "":
                    return 0
                length = 0 if count <= 1 else len(str(count))
                return  length + 1
            
            
            
            if s[index] == last_character:
                
                return min(dp(index+1,last_character,count+1,k),
                           dp(index+1,last_character,count,k-1))
            else:
                
                if last_character == "":
                    
                    return min(dp(index+1,s[index],1,k),
                           dp(index+1,last_character,count,k-1))
                else:
                    length = 0 if count <= 1 else len(str(count))
                    return min(length + 1 + dp(index+1,s[index],1,k),
                               dp(index+1,last_character,count,k-1))
        
        return dp(0,"",0,k)
            
                           
            
            