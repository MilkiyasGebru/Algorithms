class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        maxx = nums[-1]
        operation = 0
        
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i] > maxx:
                
                operation += math.ceil(nums[i]/maxx) - 1
                div = math.ceil(nums[i]/maxx)
                maxx =  math.floor(nums[i]/div)
                
            else:
                
                maxx = nums[i]
                
        return operation