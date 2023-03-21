class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        left = 0
        answer = 0
        
        for right in range(len(nums)):
            
            if nums[right] != 0:
                left = right + 1
            
            answer += right -left + 1
        
        return answer 
            