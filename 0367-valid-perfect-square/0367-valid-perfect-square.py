class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left = 1
        right = num + 1
        
        while left < right:
            
            mid = ( left + right )//2
            
            if mid*mid > num:
                right = mid
            
            else:
                left = mid + 1
                
        return (left-1)*(left-1) == num