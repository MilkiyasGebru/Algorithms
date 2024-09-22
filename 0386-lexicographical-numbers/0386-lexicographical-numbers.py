class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # I can not build trie
        answer = []
        start = 1
        while len(answer) < n :
            
            if start <= n:
                answer.append(start)
                start *= 10
            else:
                start //= 10
                start += 1 
                while start % 10 == 0 :
                    start //= 10
            
            
        
        
        return answer
    