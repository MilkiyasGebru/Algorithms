class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(lambda : math.inf)
        summ = 0
        ans = -math.inf
        for num in nums:
            summ += num
            prefix_sum[num] = min(prefix_sum[num],summ)
            ans = max(ans,summ - prefix_sum[num+k] + num+k, summ - prefix_sum[num-k] + num - k)
            
        return ans if ans != -math.inf else 0