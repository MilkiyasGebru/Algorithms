class Solution:
    
    def isValid(self,arr,length):
        decreasing_arr = [(math.inf,0)]
        for i in range(len(arr)-1,-1,-1):
            # while decreasing_arr and decreasing_arr[-1][0] < arr[i]:
            #     decreasing_arr.pop()
            decreasing_arr.append((arr[i],decreasing_arr[-1][1]+ (1 if decreasing_arr[-1][0] >= arr[i] else 0)))
        
        decreasing_arr.reverse()
        increasing_arr = [(0,0)]
        for i in range(len(arr)):
            right_index = i + length
            if right_index >= len(decreasing_arr):
                return False
            if increasing_arr[-1][0] <= decreasing_arr[right_index][0] and increasing_arr[-1][1] + decreasing_arr[right_index][1] == len(arr) - length:
                return True
            
            while increasing_arr and increasing_arr[-1][0] > arr[i]:
                increasing_arr.pop()
            increasing_arr.append((arr[i],increasing_arr[-1][1]+1))
        return False
    
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        left = 0
        right = len(arr)
        while left < right:
            
            mid = (left + right)//2
            
            if self.isValid(arr,mid):
                right = mid
            else:
                left = mid + 1
        return right
            
        
        