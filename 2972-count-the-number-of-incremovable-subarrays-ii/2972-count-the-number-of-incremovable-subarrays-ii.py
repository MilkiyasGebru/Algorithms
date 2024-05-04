class Solution:
    
    def binary_search(self,left,val,nums):
        
        right = len(nums)
        
        while left < right:
            
            mid = (left + right)//2
            
            if nums[mid] > val:
                right = mid
            else:
                left = mid + 1
        return left 
    
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        left = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                left = i
            else:
                break
        
        total = 0
        prev_max = 0
        for i in range(len(nums)):
            val = self.binary_search(max(left,i),prev_max,nums)
            total += len(nums)-val + (1 if val > i else 0) 
            if nums[i] <= prev_max:
                break
            prev_max = nums[i]
        return total
        