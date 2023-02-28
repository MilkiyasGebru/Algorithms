class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mini_length = len(nums)
        max_value = max(Counter(nums).values())
        f = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            f[nums[right]] += 1
            
            while(f[nums[right]] == max_value):
                mini_length = min(mini_length , right - left + 1)
                f[nums[left]] -= 1
                left += 1
        
        return mini_length
            