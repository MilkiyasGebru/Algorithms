# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def binary_search_increasing(self,mountain_arr,left,right,target):
        
        while left < right:
            
            mid = (left + right)//2
            value = mountain_arr.get(mid)
            
            if value >= target:
                right = mid
            else:
                left = mid + 1
        return math.inf if left == mountain_arr.length() or mountain_arr.get(left) != target else left
    def binary_search_decreasing(self,mountain_arr,left,right,target):
        
        while left < right:
            
            mid = (left + right)//2
            
            if mountain_arr.get(mid)  <= target:
                right = mid
            else:
                left = mid + 1
        
        return math.inf if left == mountain_arr.length() or mountain_arr.get(left) != target else left   
        
    
        
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        '''
        I am Given A moutain Array... which is a two sorted array joined. one in descending 
        the other ascending.

        I am thinking of binary search but how would I find the pivot point???

        '''
        
        #Lets first find the peak element
        
        left = 1
        right = mountain_arr.length()-1
        while left < right:
            
            mid = (left + right) // 2
            val1,val2,val3 = mountain_arr.get(mid-1),mountain_arr.get(mid),mountain_arr.get(mid+1)
            
            if val1 < val2 > val3:
                left = mid 
                break
            elif val1 < val2 < val3:
                left = mid + 1
            else:
                right = mid 
        possible_index = min(self.binary_search_increasing(mountain_arr,0,left+1,target),
                            self.binary_search_decreasing(mountain_arr,left,mountain_arr.length(),target))
        return possible_index if possible_index != math.inf else -1