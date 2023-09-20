class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        f = defaultdict(lambda : -math.inf)
        total = 0
        
        f[0] = len(nums) 
        for i in range(len(nums)-1,-1,-1):
            
            total += nums[i]
            f[total] = i
            
        answer = len(nums) - f[x]
        total = 0
        for i in range(len(nums)):
            total += nums[i] 
            if f[x-total] > i:
                answer = min(i+1 + len(nums) - f[x-total],answer)
        
        return answer if answer != math.inf else -1
        
        