class Solution:
    def binary_search(self,nums,left,target):
        left = left 
        right = len(nums)
        
        while left < right:
            
            mid = (left + right)//2
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return len(nums) - left
    
    def minOperations(self, nums: List[int]) -> int:
        duplicates = 0
        answer = inf
        nums.sort()
        new_array = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != new_array[-1]:
                new_array.append(nums[i])
            
            if nums[i-1] == nums[i]:
                duplicates += 1
        
        for i in range(len(new_array)):
            answer = min(answer,i + self.binary_search(new_array,i,new_array[i]+len(nums)-1))
        
        return answer + duplicates