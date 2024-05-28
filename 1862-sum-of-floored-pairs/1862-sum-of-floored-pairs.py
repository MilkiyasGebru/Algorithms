class Solution:
    
    def binarySearch(self,left,nums,val,prefix,freq):
        
        right = len(nums)
        while left < right:
            
            mid = (left + right)//2
            
            if nums[mid] >= val:
                right = mid
            else:
                left = mid + 1
        
        if left < len(prefix):
            prefix[left] += freq
            prefix[left] %= (10**9 + 7)
    
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        
    
        
        
        freq = Counter(nums)
        prefix = [0 for _ in range(len(nums))]
        nums.sort()
        
        for i in range(len(nums)):
            count = 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while count*nums[i] <= nums[-1]:
                self.binarySearch(i,nums,count*nums[i],prefix,freq[nums[i]])
                count += 1
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
            prefix[i] %= (10**9 + 7)
        return sum(prefix)%(10**9 + 7)
            
            
        