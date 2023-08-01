class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.answer = []
        
        def backTrack(i,arr):
            
            if len(arr) == k or len(arr) + n - i + 1 < k:
                
                if len(arr) == k:
                    self.answer.append(arr.copy())
                
                return 
            
            for index in range(i,n+1):
                
                backTrack(index+1,arr+[index])
        
        backTrack(1,[])
        return self.answer
            
            