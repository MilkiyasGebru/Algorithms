class Solution:
    
    def isValid(self,quantities,value):
        
        total = 0
        for quantity in quantities:
            total += math.ceil(quantity/value)
        return total
    
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        
        left = 1
        right = max(quantities)+1
        
        while left < right:
            
            mid = (left + right)//2
            if n >= self.isValid(quantities,mid):
                right = mid 
            else:
                left = mid + 1
        
        return right