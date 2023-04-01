class Solution:
    
    def isValid(self,f):
        
        for key in f.keys():
            if f[key] > 1:
                return False
        
        return True
    
    
    
    def maxLength(self, arr: List[str]) -> int:
        
        
        self.answer = 0
        
        def backTrack(index,f):
            
            self.answer = max(sum(f.values()),self.answer)
            
            if index == len(arr):
                return 
            
            for i in range(index,len(arr)):
                
                if self.isValid(f + Counter(arr[i])):
                    backTrack(i+1,f + Counter(arr[i]))
                              
        backTrack(0,Counter())
        return self.answer
        
            
            
            