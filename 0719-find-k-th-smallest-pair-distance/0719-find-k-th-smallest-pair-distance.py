class Solution:
    
    def calc(self,nums,dist):
        left = 0
        count = 0
        for right in range(len(nums)):
            
            while(nums[right] - nums[left] > dist):
                left+=1
            count += right - left
        return count
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        high = nums[-1]-nums[0]
        low = inf
        
    
        
        for i in range(1,len(nums)):
            
            low = min(nums[i]-nums[i-1],low)
            
        while(low <= high):
            
            mid = ( low + high)//2
            
            if self.calc(nums,mid) >= k :
                high = mid - 1
                
            else:
                low = mid + 1
                
        return low
                
        
        
        