class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    arr[i] = max(1+ arr[j],arr[i])
        
        return max(arr)