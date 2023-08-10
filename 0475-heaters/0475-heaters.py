class Solution:
    def binary_search(self,heaters,house):
        
        mini_distance = math.inf
        left,right = 0,len(heaters)
        
        while left < right:
            mid = (left + right)//2
            
            mini_distance = min(mini_distance,abs(heaters[mid]-house))
            
            if heaters[mid] >= house:
                right = mid
                
            else:
                left = mid + 1
                
        return mini_distance
                
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        radius = 0
        
        for house in houses:
            radius = max(radius, self.binary_search(heaters,house))
        
        return radius
        
        