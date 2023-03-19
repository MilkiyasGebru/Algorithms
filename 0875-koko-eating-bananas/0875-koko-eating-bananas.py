class Solution:
    
    def condition(self,piles,k):
        total = 0
        for pile in piles:
            
            total += math.ceil(pile/k)
        
        return total
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left,right = 1,max(piles)
        
        while left < right:
            
            mid = (left + right)//2
            
            if self.condition(piles,mid) <= h:
                
                right = mid 
            
            else:
                
                left = mid + 1
        
        return left 
            