class Solution:
    def binary_search(self,events,end):
        left = 0 
        right = len(events)
        
        while left < right:
            mid = (left + right)//2
            
            if events[mid][0] > end:
                right = mid 
            else:
                left = mid + 1
        return left 
    
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        
        @cache
        def dp(index,k):
            
            if index >= len(events) or k == 0:
                return 0
            
            return max(events[index][-1] + dp(self.binary_search(events,events[index][1]),k-1), dp(index+1,k))
        
        return dp(0,k)