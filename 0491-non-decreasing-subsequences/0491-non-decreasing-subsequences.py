class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.answer = set()
        
        def backtrack(index,ans):
            
            if len(ans) >= 2:
                self.answer.add(tuple(ans))
            for i in range(index,len(nums)):
                
                if ans == [] or nums[i] >= ans[-1]:
                    backtrack(i+1,ans+[nums[i]])
        
        backtrack(0,[])
        return self.answer