class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        # Handle the edge case
        
        if len(nums) == 1 :
            return -1 if k%2 == 1 else nums[0]
        
        nums.append(-math.inf)
        answer = stack = -math.inf
        
        for i in range(len(nums)):
            
            if k > 0:
                answer = max(answer,stack)
            if k == 0:
                answer = max(answer,nums[i])
            stack = max(nums[i],stack)
            k -= 1
        
        
        return answer if answer != -math.inf else -1