class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left = 0
        answer = 0
        for right in range(len(nums)):
            
            while nums[right] > nums[left] + 2*k:
                left += 1
            
            answer = max(answer, right - left + 1)
        
        return answer
        