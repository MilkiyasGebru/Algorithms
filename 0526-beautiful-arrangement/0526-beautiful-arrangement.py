class Solution:
    def countArrangement(self, n: int) -> int:
        visited = 0
        # Set bit A |= 1 << bit
# Clear bit A &= ~(1 << bit)
        def backTrack(i):
            
            if i == n+1:
                
                return 1
            ans = 0
            nonlocal visited
            
            for num in range(1,n+1):
                if (visited & (1 << num) == 0) and (i % num == 0 or num %i == 0):
                    
                    visited |= 1 << num
                    ans += backTrack(i+1)
                    visited &= ~(1 << num)
            
            return ans
        
        return backTrack(1)
        
        