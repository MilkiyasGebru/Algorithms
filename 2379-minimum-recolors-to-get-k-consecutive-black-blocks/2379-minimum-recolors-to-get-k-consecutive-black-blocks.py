class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minRecolor = 0
        
        left = 0
        count = 0
        mini_answer= len(blocks)
        
        for right in range(len(blocks)):
            
            if blocks[right] == "W":
                count += 1
                
            while(right - left + 1 == k):
                
                mini_answer = min(count,mini_answer)
                
                count -= 1 if blocks[left]=="W" else 0
                left += 1
        
        return mini_answer
                
                
                
                