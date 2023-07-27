class Solution:
    
    def binary_search(self,dist,speed):
        
        total_hour = 0
        for i in range(len(dist)-1):
            
            total_hour += math.ceil(dist[i]/speed)
        
        return total_hour + dist[-1]/speed
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        if len(dist)-1 >= hour:
            return -1
        
        left,right = 1,max(max(dist),100*dist[-1])+1
        while left < right:
            
            mid = (left + right) // 2
            
            if self.binary_search(dist,mid) <= hour:
                right = mid 
            else:
                left = mid + 1
        
        return left
    