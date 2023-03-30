class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache(None)
        def rec(s,left,right):
            
            if s == "" or s2[left:right+1] == "":
                return False
                
            if s == s2[left:right+1]:
                return True
            
            x = False
            
            for i in range(1,len(s)):
                
                l1 = i 
                l2 = len(s)-i
                
                unscrambled = rec(s[:i],left,left + l1 - 1) and rec(s[i:],right-l2+1,right)
                scrambled = rec(s[i:],left,left+l2-1) and rec(s[:i],right-l1+1,right)

                x = x or unscrambled or scrambled
                
            return x
        
        return rec(s1,0,len(s2)-1)
        