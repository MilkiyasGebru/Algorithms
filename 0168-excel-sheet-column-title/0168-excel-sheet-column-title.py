class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        answer = []
        
        while(columnNumber > 0):
            
            columnNumber -= 1
            div = columnNumber%26
            answer.append(chr(ord("A") + div ))
            columnNumber //= 26
            
        answer.reverse()
        return "".join(answer)