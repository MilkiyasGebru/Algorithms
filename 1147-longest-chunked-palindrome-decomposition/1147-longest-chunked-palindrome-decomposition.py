class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        
        left = 0
        right = len(text)
        answer = 0
        while left < right:
            found = False
            for i in range(1,len(text)):
                
                if left+i <= right-i and text[left:left+i] == text[right-i:right]:
                    found = True
                    answer += 2
                    left = left + i
                    right = right - i
                    
                    break
                elif left + i >= right-i:
                    break
            
            if not found:
                return answer + 1
        
        return answer
                
        