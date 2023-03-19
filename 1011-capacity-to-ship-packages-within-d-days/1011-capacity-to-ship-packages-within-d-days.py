class Solution:
    
    def condition(self,weights,maxx,days):
        
        total = day =  0
        
        for weight in weights:
            
            if total + weight > maxx:
                
                day += 1
                total = 0
                
            total += weight
        day += 1 if total != 0 else 0
        
        return day <= days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            
            mid = (left + right )//2
            
            if self.condition(weights,mid,days):
                
                right = mid
                
            else:
                
                left = mid + 1
        
        return left 
        
        