class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates.sort()
        
        self.answer = []
        def backtrack(index,path,target):
            
            if target == 0:
                self.answer.append(path)
                
            if target < 0 or index >= len(candidates) or candidates[index] > target  :
                return
            
            for i in range(index,len(candidates)):
                
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                backtrack(i+1,path+[candidates[i]],target-candidates[i])
        
        backtrack(0,[],target)
        return self.answer