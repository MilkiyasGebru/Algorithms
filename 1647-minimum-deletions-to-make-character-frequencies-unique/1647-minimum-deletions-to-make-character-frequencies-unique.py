class Solution:
    def minDeletions(self, s: str) -> int:
        
        f = Counter(Counter(s).values())
        maxx = max(f.keys())
        answer = 0
        for i in range(maxx,0,-1):
            
            if f[i] > 1:
                answer += f[i] - 1
                f[i-1] += f[i] - 1
        
        return answer