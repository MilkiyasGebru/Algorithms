class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        dp = defaultdict(lambda : 1)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                diff = nums[j]-nums[i]
                    
                dp[(i,diff)] = max(dp[(i,diff)], 1 + dp[(j,diff)])
        
        
        return max(dp.values())
        
            