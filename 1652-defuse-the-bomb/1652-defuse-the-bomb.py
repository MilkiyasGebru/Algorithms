class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        prefix = []
        answer = []
        
        if k < 0 :
            code.reverse()
            
            
        for j in range(2):
            for i in range(len(code)):
                if not prefix:
                    prefix.append(code[i])
                else:
                    prefix.append(prefix[-1] + code[i])
        
        for i in range(len(code)):
            
            answer.append(prefix[i+abs(k)]-prefix[i])
        if k < 0:
            answer.reverse()
        return answer
            