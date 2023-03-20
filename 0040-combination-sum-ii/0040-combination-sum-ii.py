class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        answer = set()
        path = set()
        
        def backtrack(i,total,arr):
            if i == len(candidates) or total == target:
                if total == target:
                    answer.add(tuple(arr.copy()))
                return
            if tuple(arr.copy()) in path:
                return
            path.add(tuple(arr.copy()))
            
            for j in range(i,len(candidates)):
                
                if total + candidates[j] > target:
                    
                    return 
                
                backtrack(j+1,total+candidates[j],arr + [candidates[j]])
        
        backtrack(0,0,[])
        return answer