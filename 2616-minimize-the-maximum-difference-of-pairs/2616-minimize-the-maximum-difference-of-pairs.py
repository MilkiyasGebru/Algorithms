class Solution:
    
    def countPairs(self,nums,diff):
        
        totalPairs = 0
        i = 0
        while i < len(nums)-1:
            if nums[i+1] - nums[i] <= diff:
                totalPairs += 1
                i += 1
            i += 1
        
        return totalPairs
        
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        left,right = 0, nums[-1] - nums[0] + 1
        
        while left < right:
            
            mid = (left + right) //2 
            
            if self.countPairs(nums,mid) >= p:
                right = mid
            else:
                left = mid + 1
        
        return left