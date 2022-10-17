class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        left = 0
        right = len(height)-1
        while(left < right):
            
            if left >= right:
                break
            maxArea = max( maxArea, min(height[left],height[right])*(right-left))
            
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return maxArea
            