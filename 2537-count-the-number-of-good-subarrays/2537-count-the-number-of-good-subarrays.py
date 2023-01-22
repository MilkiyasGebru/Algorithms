class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        f = defaultdict(int)
        f[nums[left]]+=1
        ans = 0
        count = 0
        
        for right in range(1,len(nums)):
            
            count += f[nums[right]] 
            f[nums[right]] += 1
            while(count >= k):
                
                ans += len(nums) - right
                count -= f[nums[left]] - 1
                f[nums[left]] -= 1
                left += 1
        return ans
            