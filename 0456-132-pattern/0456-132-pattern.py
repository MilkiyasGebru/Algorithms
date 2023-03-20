class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        minimums = [nums[0]]
        stack = []
        
        for i in range(1,len(nums)):
            
            minimums.append(min(nums[i],minimums[-1]))
        
        
        for i in range(len(nums)):
            
            while (stack and nums[stack[-1]] <= nums[i]):
                
                stack.pop()
            
            if stack and minimums[stack[-1]] < nums[i] < nums[stack[-1]]:
                return True
            
            stack.append(i)
        
        return False
                
                