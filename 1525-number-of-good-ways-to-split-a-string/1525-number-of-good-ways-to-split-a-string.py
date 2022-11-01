class Solution:
    def numSplits(self, s: str) -> int:
        
        forward_letters = set()
        backward_letters = {}
        
        
        for i in range(len(s)-1,-1,-1):
            
            if s[i] not in backward_letters:
                backward_letters[s[i]] = 0
                
            backward_letters[s[i]]+=1
                
        good_splits = 0
        
        for i in range(len(s)):
            
            forward_letters.add(s[i])
            backward_letters[s[i]]-=1
            
            if backward_letters[s[i]]==0:
                del backward_letters[s[i]]
                
            if len(forward_letters) == len(backward_letters):
                good_splits += 1
            
            
        return good_splits