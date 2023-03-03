class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        monotonic_stack = []
        answer = 0
        mod = 10**9 + 7
        
        for num in nums:
            
            prev = 0
            
            while( len(monotonic_stack) > 0 and monotonic_stack[-1][0] >= num ):
                
                prev += monotonic_stack[-1][1]
                answer = max(answer, (monotonic_stack[-1][0] * prev))
                monotonic_stack.pop()
                
            monotonic_stack.append((num,num+prev))
            
        prev = 0
        
        for i in range(len(monotonic_stack)-1,-1,-1): 
            
            prev +=  monotonic_stack[i][1]
            answer = max(answer, (monotonic_stack[i][0]*prev))
        
        
        return answer%mod