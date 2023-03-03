class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        monotonic_stack = []
        answer = 0
        mod = 10**9 + 7
        nums.append(0)
        for num in nums:
            
            prev = 0
            
            while( len(monotonic_stack) > 0 and monotonic_stack[-1][0] >= num ):
                
                prev += monotonic_stack[-1][1]
                answer = max(answer, (monotonic_stack[-1][0] * prev))
                monotonic_stack.pop()
                
            monotonic_stack.append((num,num+prev))
            

        
        
        return answer%mod