class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = max(nums)
        left = answer = 0
        for right in range(len(nums)):
            if nums[right] != maxx:
                left = right + 1
            
            answer = max(answer, right - left + 1)
        
        return answer