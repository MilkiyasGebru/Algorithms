class Solution:
    
    def is_condition(self,start,x,d):
        start = start.copy()
        # print(start)
        for i in range(1,len(start)):
            if start[i] - start[i-1] + d < x:
                return False
            start[i] = max(start[i],start[i-1]+x)
        # print(start)
        
        return True
        
    
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        
        start.sort()
        # start[-1] += d
        
        left = 0
        right = start[-1] - start[0] + d + 1
        while left < right:
            
            mid = (left + right)//2
            
            if self.is_condition(start,mid,d):
                left = mid + 1
            else:
                right = mid
            
        return left - 1