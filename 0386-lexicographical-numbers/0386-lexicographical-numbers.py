class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # I can not build trie
        answer = []
        start = 1
        while start :
            if answer and str(answer[-1]) >= str(start):
                break
            if start <= n:
                answer.append(start)
                start *= 10
            else:
                start //= 10
                start += 1 
                while start % 10 == 0 :
                    start //= 10
            
            
        
        
        return answer
    