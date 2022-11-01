class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        size = len(arr)//k
        @lru_cache(None)
        
        def dp(index,size,maxx):
            
            if index == len(arr):
                
                return maxx*size
            
            if k == size:
                return size*maxx + dp(index+1,1,arr[index])    
            
            return max( max(maxx , arr[index])*(size + 1)  + dp(index+1,0,0), dp(index+1,size+1,max(maxx , arr[index])))
        
        return dp(0,0,0)
            