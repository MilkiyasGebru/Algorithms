class Solution:
    
    def check_condition(self,position,dist):
        total = 0
        inital = position[0]
        for i in range(1,len(position)):
            if position[i] - inital >= dist:
                total += 1
                inital = position[i]
        return total
    
    def maxDistance(self, position: List[int], m: int) -> int:
        
        # T T T T T T F F F F
        position.sort()
        left = 0
        right = position[-1] - position[0] + 1
        
        while left < right:
            
            mid = (left + right)//2
            
            if self.check_condition(position,mid) >= m-1:
                left = mid + 1
                
            else:
                right = mid 
        return left - 1
                
        