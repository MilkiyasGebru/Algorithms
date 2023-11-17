class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        answer = -math.inf
        for i in range(len(nums)//2):
            answer = max(answer, nums[i]+nums[-i-1] )
        
        return answer