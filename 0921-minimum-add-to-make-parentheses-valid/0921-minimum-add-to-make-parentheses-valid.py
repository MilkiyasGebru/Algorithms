class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mini_length = 0
        count = 0
        
        for i in s:
            
            if i == "(":
                count += 1
                
            else:
                
                count -= 1
                
                if count < 0:
                    
                    count = 0
                    mini_length += 1
        
        return mini_length + count