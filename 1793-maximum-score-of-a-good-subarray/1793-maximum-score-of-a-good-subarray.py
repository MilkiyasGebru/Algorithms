class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        nums.append(-math.inf)
        score = 0
        min_stack = []
        
        for right in range(len(nums)):
            
            left = math.inf
            
            while min_stack and min_stack[-1][0] > nums[right]:
                
                value,left = min_stack.pop()
                
                
                if left <= k and right > k:
                    score = max(score, value*(right - left ))
                    
            min_stack.append((nums[right],min(right,left)))
        
        return score
            