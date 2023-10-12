# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        def find_pivot():
            
            left = 1
            right = mountain_arr.length() - 1
            
            while left < right:
                
                mid = (left + right) // 2
                
                if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                    
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        
        def find_increasing_array():
            left = 0
            right = pivot_index + 1
            
            while left < right:
                
                mid = (left + right)//2
                
                if mountain_arr.get(mid) >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return math.inf if mountain_arr.get(left) != target else left
        
        def find_decreasing_array():
            left = pivot_index
            right = mountain_arr.length()
            
            while left < right:
                mid = (left + right)//2
                if mountain_arr.get(mid) <= target:
                    right = mid
                else:
                    left = mid + 1
            return math.inf if left >= mountain_arr.length() or target != mountain_arr.get(left) else left
        pivot_index = find_pivot()
        min_index = min(find_increasing_array(),find_decreasing_array())
        return min_index if min_index != math.inf else -1
            
                
                