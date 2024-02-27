class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.answer = []
        def backtrack(arr,left,right):
            
            if right > left or left > n:
                return
            
            if len(arr) == 2*n:
                self.answer.append("".join(arr))
                return
            
            backtrack(arr+["("],left+1,right)
            backtrack(arr+[")"],left,right+1)
        
        backtrack([],0,0)
        return self.answer
                
                
            
        