class Solution:
    
    def convert(self,char):
        return ord(char)-ord("a") + 1
    
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        
        power = 1
    
        input_hash = 0
        rolling_hash = 0
        
        for i in range(len(needle)):
            
            input_hash += self.convert(needle[i]) * power 
            rolling_hash += self.convert(haystack[i]) * power
            power*=31
            
        power//=31   
        
        if rolling_hash == input_hash:
            return 0
        
        left = 0
        for right in range(len(needle),len(haystack)):
            
            rolling_hash -= self.convert(haystack[left])
            rolling_hash //=31
            rolling_hash += self.convert(haystack[right])*power
            left+=1
            
            if rolling_hash == input_hash:
                return left
            
        return -1