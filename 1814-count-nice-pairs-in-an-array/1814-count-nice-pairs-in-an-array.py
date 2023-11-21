class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        
        f = defaultdict(int)
        ans = 0
        mod = 10**9 + 7
        for num in nums:
            
            ans += f[num - int(str(num)[::-1])]
            f[num - int(str(num)[::-1])] += 1
            ans %= mod
        return ans