class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        total = total // 2
        dp = [[False for i in range(total + 1)] for i in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][total] = True
        
        for i in range(len(nums)-2,-1,-1):
            for s in range(total,-1,-1):
                
                if s + nums[i] <= total:
                    dp[i][s] = dp[i+1][s] or dp[i+1][s+nums[i]]
                else:
                    dp[i][s] = dp[i+1][s]
        return dp[0][0]
                
        
       