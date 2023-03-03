class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        f = {}
        
        arr = []
        answer = []
        
        for i in range(len(nums)):
            
            while ( len(arr) > 0 and nums[arr[-1]] < nums[i]):
                
                f[arr[-1]] = nums[i]
                arr.pop()
                
            arr.append(i)
            
        for i in range(len(nums)):
            
            while( len(arr) > 0 and nums[arr[-1]] < nums[i]):
                
                f[arr[-1]] = nums[i]
                arr.pop()
        
            
        for i in range(len(nums)):
            
            if i in f:
                answer.append(f[i])
            else:
                answer.append(-1)
        
        return answer
            