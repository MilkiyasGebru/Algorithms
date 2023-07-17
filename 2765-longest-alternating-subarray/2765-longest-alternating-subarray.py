class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        length = 1
        maxLength = -1
        diff = 1
        for index in range(1,len(nums)):
            if nums[index] - nums[index-1] == diff:
                diff *= -1
                length += 1
            else:
                length = 1 if nums[index] - nums[index-1] != 1 else 2
                diff = 1 if nums[index] - nums[index-1] != 1 else -1
            maxLength = max(maxLength,length)
        
        return maxLength if maxLength > 1 else -1
        