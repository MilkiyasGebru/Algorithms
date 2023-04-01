class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        visited =  set()
        
        
        def backTrack(index,path):
            
            if len(path) > 1:
                visited.add(tuple(path))
            
            if index == len(nums):
                return
            
            for i in range(index,len(nums)):
                
                if (not path or path[-1] <= nums[i]) and tuple(path + [nums[i]]) not in visited:
                    backTrack(i+1,path+[nums[i]])
        
        backTrack(0,[])
        return visited