class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        f[0]=1
        pre=0
        ans = 0
        for i in range(len(nums)):
            pre += nums[i]
            ans += f[pre%k]
            f[pre%k]+=1
        return ans