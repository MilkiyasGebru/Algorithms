class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = max_subarray = 0
        count = 0
        for right in range(len(nums)):
            
            count += 1 if nums[right] == 0 else 0
            while count > 1:
                count -= 1 if nums[left] == 0 else 0
                left += 1
            
            max_subarray = max(max_subarray,right - left )
        
        return max_subarray