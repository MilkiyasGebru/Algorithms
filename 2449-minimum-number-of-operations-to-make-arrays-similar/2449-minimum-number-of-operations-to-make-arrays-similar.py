class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
        nums.sort()
        target.sort()
        
        up = 0
        even_pointer,odd_pointer = 0,0
        
        for i in range(len(nums)):
            
            if nums[i] % 2 == 0:
                
                while even_pointer < len(target) and target[even_pointer] %2 != 0:
                    even_pointer += 1
                
                up += max( (target[even_pointer] - nums[i])//2,0)
                even_pointer += 1
                
            else:
                
                while odd_pointer < len(target) and target[odd_pointer] %2 == 0:
                    odd_pointer += 1
                
                
                up += max((target[odd_pointer] - nums[i])//2,0)
                odd_pointer += 1
        
        return up
        
        
     
        
        
        
        
        