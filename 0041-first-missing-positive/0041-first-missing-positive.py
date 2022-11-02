class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            if num > 0 and num <= len(nums):
                mask |= (1 << num)
        mask >>= 1
        return int(log2((mask|(mask+1))^(mask))) + 1