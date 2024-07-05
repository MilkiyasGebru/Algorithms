class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 0
        ans = nums[-1] - nums[3]
        for i in range(3):
            ans = min(ans,nums[-(3-i+1)] - nums[i] )
        return ans