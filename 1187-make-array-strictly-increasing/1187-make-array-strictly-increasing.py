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
            
            cost = math.inf
            if arr1[i] > prev_max:
                cost = dp(i+1,arr1[i])
            
            idx = self.binarySearch(arr2,prev_max)
            if idx < len(arr2):
                cost = min(1+dp(i+1,arr2[idx]),cost)
            
            return cost
        min_cost = dp(0,-math.inf)
            
        return min_cost if min_cost != math.inf else -1
        

            
            