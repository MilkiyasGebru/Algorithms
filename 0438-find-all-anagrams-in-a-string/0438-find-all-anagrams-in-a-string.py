class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        
        f = defaultdict(int)
        g = defaultdict(int)
        
        for i in range(len(p)):
            
            f[p[i]] += 1
        answer = []
        for right in range(len(s)):
            
            g[s[right]] += 1
            
            while(g[s[right]] > f[s[right]]):
                
                g[s[left]] -= 1
                left += 1
            
            if right - left + 1 == len(p):
                answer.append(left)
        
        return answer