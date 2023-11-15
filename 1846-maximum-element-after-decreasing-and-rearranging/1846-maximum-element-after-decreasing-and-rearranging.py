class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        prev = 1
        for i in range(1,len(arr)):
            if arr[i] > prev:
                prev = prev + 1
        
        return prev
        