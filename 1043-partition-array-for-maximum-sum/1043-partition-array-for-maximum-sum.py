class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @cache
        def dp(index,count,max_index):
            
            if index == len(arr):
                return count*arr[max_index]
            
            if count == k:
                return count*arr[max_index] + dp(index+1,1,index)
            
            return max(count*arr[max_index] + dp(index+1,1,index), dp(index+1,count+1,index if arr[index] > arr[max_index] else max_index))
        
        return dp(0,0,0)
        
                     