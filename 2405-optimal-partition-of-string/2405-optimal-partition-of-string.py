class Solution:
    def partitionString(self, s: str) -> int:
        
        last = defaultdict(lambda  : -1)
        last_partion = 0
        partions = 1
        
        for i in range(len(s)):
            
            if last[s[i]] >= last_partion:
                
                last_partion = i
                partions += 1
                
            last[s[i]] = i
        
        return partions
        