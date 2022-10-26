class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(left, right):
            if left > right:
                return 0
            return max(nums[left]-dp(left+1, right), nums[right] - dp(left, right-1))
        return dp(0, len(nums)-1) > -1