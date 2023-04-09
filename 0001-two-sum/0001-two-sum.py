class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = {}
        for i in range(len(nums)):
            f[nums[i]]=i
        
        for i in range(len(nums)):
            if (target - nums[i]) in f and f[target-nums[i]] != i:
                return [i,f[target-nums[i]]]
                
        