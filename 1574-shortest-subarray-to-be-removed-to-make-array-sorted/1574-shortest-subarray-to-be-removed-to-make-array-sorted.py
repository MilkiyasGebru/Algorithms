class Solution:
    def binary_search(self,left,val, arr):
        right = len(arr)
        while left < right:
            mid = (left + right)//2
            
            if arr[mid] >= val:
                right = mid
            else:
                left = mid + 1
        return left
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        left = len(arr)-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] <= arr[i+1]:
                left = i
            else:
                break
        
        prev_max = -math.inf
        answer = len(arr)
        for i in range(len(arr)):
            
            answer = min(self.binary_search(max(left,i),prev_max,arr)-i,answer)
            if prev_max > arr[i]:
                break
            prev_max = max(arr[i],prev_max)
        return answer
            
        
        