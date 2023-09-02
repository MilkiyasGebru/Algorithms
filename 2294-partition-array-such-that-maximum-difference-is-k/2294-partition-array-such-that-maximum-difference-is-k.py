class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        partitions = 1
        nums.sort()
        minn = nums[0]
        
        for i in range(len(nums)):
            if nums[i] - minn > k:
                partitions += 1
                minn = nums[i]
        
        return partitions