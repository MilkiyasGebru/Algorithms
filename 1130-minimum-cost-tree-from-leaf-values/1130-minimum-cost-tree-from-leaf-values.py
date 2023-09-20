class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @cache
        def dp(left,right):
            
            if left == right:
                return 0
        
            # left_pick
            answer = math.inf
            maxx = arr[left]
            
            for i in range(left,right):
                
                maxx = max(arr[i],maxx)
                answer = min( answer, maxx*max(arr[i+1:right+1]) + dp(left,i) + dp(i+1,right))
            
            return answer
        
        return dp(0,len(arr)-1)
                