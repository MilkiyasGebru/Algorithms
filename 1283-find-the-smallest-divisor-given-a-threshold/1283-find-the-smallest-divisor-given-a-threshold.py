class Solution:
    def calculate_threshold(self,nums,divisor):
        
        total_threshold = 0
        for num in nums:
            total_threshold += math.ceil(num/divisor)
        return total_threshold
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left,right = 1,max(nums)+1
        
        while left < right:
            
            mid = (left + right) //2
            
            if self.calculate_threshold(nums,mid) <= threshold:
                
                right = mid 
            else:
                left = mid + 1
        
        return left
        