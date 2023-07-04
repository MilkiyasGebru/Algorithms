class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        dp = defaultdict(lambda : 1)
        dp[(0,0)] = 1
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                diff = nums[j]-nums[i]
                if diff != 0:
                    
                    dp[(nums[i],diff)] = max(dp[(nums[i],diff)], 1 + dp[(nums[j],diff)])
        
        
        return max(max(dp.values()),max(Counter(nums).values()))
        
            