class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        
        for i in range(n//2):
            answer.append(i+1)
            answer.append(-(i+1))
        
        if n%2 == 1:
            answer.append(0)
        
        return answer
        