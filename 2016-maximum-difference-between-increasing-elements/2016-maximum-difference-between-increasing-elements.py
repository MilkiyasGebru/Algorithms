class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -inf
        min_value = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > min_value:
                answer = max(answer,nums[i]-min_value)
            else:
                min_value = min(min_value,nums[i])
        
        return answer if answer != -inf else -1