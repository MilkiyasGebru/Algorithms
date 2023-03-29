class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num1 = 0
        for i in range(len(nums)):
            num1 ^= i ^ nums[i]
            
        return num1^len(nums)