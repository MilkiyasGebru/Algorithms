class Solution:
    
    def is_condition(self,start,x,d):
        
        value = start[0]
        
        for i in range(1,len(start)):
            
            if start[i] - value + d < x:
                return False
            value = max(start[i],value+x)
        
        return True
        
    
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        
        start.sort()
        
        left = 0
        right = start[-1] - start[0] + d + 1
        
        while left < right:
            
            mid = (left + right)//2
            
            if self.is_condition(start,mid,d):
                left = mid + 1
            else:
                right = mid
            
        return left - 1