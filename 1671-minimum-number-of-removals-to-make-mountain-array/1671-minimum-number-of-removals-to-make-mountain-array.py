class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        
        decreasing = [0 for _ in range(len(nums))]
        increasing = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    increasing[i] = max(increasing[i],increasing[j]+1)
        
        for i in range(len(nums)-1,-1,-1):
            
            for j in range(i+1,len(nums)):
                
                if nums[i] > nums[j]:
                    decreasing[i] = max(decreasing[j]+1,decreasing[i])
        
        min_removals = math.inf
        for i in range(1,len(nums)-1):
            
            if increasing[i] and decreasing[i] :
                min_removals = min(len(nums) - decreasing[i] - increasing[i] - 1,min_removals)
        
        return min_removals
                