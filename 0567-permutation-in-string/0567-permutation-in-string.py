class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        
        f = defaultdict(int)
        g = defaultdict(int)
        for i in range(len(s1)):
            f[s1[i]] += 1
        
        for right in range(len(s2)):
            
            g[s2[right]] += 1
            
            while(g[s2[right]] > f[s2[right]]):
                
                g[s2[left]] -= 1
                
                left += 1
            
            if right - left + 1 == len(s1):
                return True
        
        return False