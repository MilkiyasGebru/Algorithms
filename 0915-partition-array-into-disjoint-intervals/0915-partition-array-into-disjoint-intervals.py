class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        right_min = [0 for _ in range(len(nums))]
        prev_min = float("inf")
        max_ = 0
        
        for i in range(len(nums)-1,-1,-1):
            
            prev_min = min(prev_min,nums[i])
            right_min[i] = prev_min
            
        for i in range(len(nums)-1):
            
            max_ = max(max_,nums[i])
            
            if max_ <= right_min[i+1]:
                return i + 1
            
