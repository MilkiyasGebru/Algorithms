class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        f = defaultdict(int)
        
        for c in s:
            f[c] += 1
        for c in t:
            f[c] -= 1
        answer = 0
        for key in f.keys():
            
            answer += max(f[key],0)
        
        return answer