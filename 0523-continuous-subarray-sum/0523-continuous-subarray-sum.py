class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        f = defaultdict(lambda:inf)
        f[0]=0
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            
            if i-f[(pre%k)]+1>=2:
                return True
            f[pre%k]=min(i+1,f[pre%k])
        return False
        