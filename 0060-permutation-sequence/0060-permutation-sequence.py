class Solution:
    
    @lru_cache(None)
    def factorial(self,n):
        if n <= 1:
            return 1
        
        return n*self.factorial(n-1)
    
    def findMax(self,curr,n):
        total = 0
        for i in range(curr,n+1):
            remain = n-i
            total += remain*self.factorial(remain)
        return total
    
    def getPermutation(self, n: int, k: int) -> str:
        
        self.answer = None
        def backTrack(i,count,arr):
            
            if count > k or self.answer or count + self.findMax(i,n) < k  :
                return self.answer
            
            if i == n+1:
                self.answer = "".join(arr)  
                return self.answer
            
            less = 0
            
            for num in range(1,n+1):
                
                if str(num) not in arr:
                    remain = n - i
                    backTrack(i+1,count + less*self.factorial(remain),arr+[str(num)])
                    less += 1
        
        backTrack(1,1,[])
        return self.answer