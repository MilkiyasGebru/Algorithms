class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        answer = 0
        heights.append(0)
        
        stack = []
        
        for height in heights:
            
            width = 0
            
            while stack and stack[-1][0] > height:
                
                val,w = stack.pop()
                width += w
                answer = max(answer,width*val)
            
            stack.append((height,width+1))
            
        return answer 
                 
                
        
        