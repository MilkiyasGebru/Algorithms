class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_stack, right_stack = [0 for _ in range(len(height))],[0 for _ in range(len(height))]
    
        left_max = right_max = 0
        
        for i in range(len(height)):
            
            left_max = max(left_max,height[i])
            left_stack[i] = left_max
            
            right_max = max(right_max,height[-(i+1)])
            right_stack[-(i+1)] = right_max
            
        max_volume = 0
        
        for i in range(len(height)):
            
            max_volume += max(0,min(left_stack[i],right_stack[i]) - height[i])
            
        return max_volume
            