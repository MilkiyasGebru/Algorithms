class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        f = {}
        
        arr = []
        answer = [-1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            
            while ( len(arr) > 0 and nums[arr[-1]] < nums[i]):
                
                answer[arr[-1]] = nums[i]
                arr.pop()
                
            arr.append(i)
            
        for i in range(len(nums)):
            
            while( len(arr) > 0 and nums[arr[-1]] < nums[i]):
                
                answer[arr[-1]] = nums[i]
                arr.pop()        
            
        
        return answer
            