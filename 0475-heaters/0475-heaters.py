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
        
        house_range = len(houses)
        heater_range = len(heaters)
        houses.sort()
        heaters.sort()

        start = 0
        ans = 0
        for i in range(house_range):
            mn = float('inf')
            for j in range(start, heater_range):
                radius = abs(houses[i] - heaters[j])
                if radius < mn:
                    start = j
                    mn = radius
                if radius > mn:
                    break
            ans = max(ans, mn)

        return ans
        
    
    
    


        