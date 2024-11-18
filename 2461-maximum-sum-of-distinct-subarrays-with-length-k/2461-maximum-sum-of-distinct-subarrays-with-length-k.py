class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        total = answer = left = 0
        freq = defaultdict(int)
        for right in range(len(nums)):
            freq[nums[right]] += 1
            total += nums[right]
            
            while freq[nums[right]] > 1:
                freq[nums[left]] -= 1
                total -= nums[left]
                left += 1
            
            if right - left + 1 == k:
                answer = max(answer,total)
                total -= nums[left]
                freq[nums[left]] -= 1
                left += 1
        return answer
                