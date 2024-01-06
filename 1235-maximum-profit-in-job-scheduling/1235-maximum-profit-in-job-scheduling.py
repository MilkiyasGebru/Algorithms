class Solution:
    def binary_search(self,arr,i):
        
        left = i + 1
        right = len(arr)
        
        while left < right:
            mid = (left + right)//2
            if arr[mid][0] >= arr[i][1]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = [(0,0,0)]
        for i in range(len(startTime)):
            arr.append((startTime[i],endTime[i],profit[i]))
        arr.sort()
        @cache
        def dp(index):
            
            if index >= len(arr):
                return 0
            return max(arr[index][2] + dp(self.binary_search(arr,index)), dp(index+1))
        
        return dp(0)