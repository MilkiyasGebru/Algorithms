class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        
        f = defaultdict(int)
        answer = 0
        for candidate in candidates:
            
            for i in range(25):
                
                if candidate & (1<<i) != 0:
                    f[i] += 1
                    answer = max(answer,f[i])
        return answer