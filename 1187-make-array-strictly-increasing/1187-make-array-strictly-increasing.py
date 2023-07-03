class Solution:
    def binarySearch(self,arr,val):
        left = 0
        right = len(arr)
        while left < right:
            
            mid = (left + right)//2
            if arr[mid] > val:
                right = mid 
            else:
                left = mid + 1
        return left 
            
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        arr1= [-math.inf ] + arr1
        f = {0:arr1,1:arr2}
        
        @cache
        def dp(i,prev_max,array):
            
            if i == len(arr1):
                return 0
            
            minn = math.inf
            
            if arr1[i] > f[array][prev_max]:
                minn = dp(i+1,i,0)
            
            next_index = self.binarySearch(arr2,f[array][prev_max])
            
            if next_index < len(arr2) and arr2[next_index] > f[array][prev_max] :
                minn = min(1 + dp(i+1,next_index,1),minn)
            
            return minn
            
        return dp(1,0,0) if dp(1,0,0) != math.inf else -1
        

            
            