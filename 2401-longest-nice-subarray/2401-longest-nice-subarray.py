class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        total_xor = 0
        left = 0 
        length = 1
        for right in range(len(nums)):
            
            while left!= right and total_xor & nums[right] != 0:
                total_xor ^= nums[left]
                left += 1
            total_xor ^= nums[right]
            length = max(right-left+1, length)
        return length
            
                
                