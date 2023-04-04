class Solution:
    def partitionString(self, s: str) -> int:
        
        prev = set()
        partions = 1
        
        for i in range(len(s)):
            if s[i] in prev:
                prev = set(s[i])
                partions += 1
            else:
                prev.add(s[i])
        
        return partions
        