class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = [0 for _ in range(n+1)]
        
        for i in range(len(answer)):
            
            answer[i] = answer[i>>1] + (i&1) 
            
        return answer