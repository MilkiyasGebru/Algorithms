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
        
        @cache
        def dp(i,prev_max):
            
            if i == len(arr1):
                return 0
            minn = math.inf
            if arr1[i] > prev_max:
                minn = dp(i+1,arr1[i])
            
            idx = self.binarySearch(arr2,prev_max)
            if idx < len(arr2):
                minn = min(1+dp(i+1,arr2[idx]),minn)
            
            return minn
            
        return dp(0,-math.inf) if dp(0,-math.inf) != math.inf else -1
        

            
            