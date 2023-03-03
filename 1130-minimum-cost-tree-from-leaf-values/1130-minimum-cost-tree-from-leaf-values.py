class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def rec(left,right):
            
            if left == right:
                return 0
            if left + 1 == right:
                return arr[left]*arr[right]
            ans = math.inf
            
            for index in range(left,right):
                ans = min(  ans ,
                          rec(left,index) + rec(index+1,right) + max(arr[left:index+1])*max(arr[index+1:right+1]))
            
            return ans
        
        return rec(0,len(arr)-1)
            