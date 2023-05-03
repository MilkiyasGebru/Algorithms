class Solution:
    
    @lru_cache(None)
    def factorial(self,n):
        if n == 1:
            return 1
        if n <= 0:
            return 0
        return n*self.factorial(n-1)
    
    def findMax(self,curr,n):
        total = 0
        for i in range(curr,n+1):
            remain = n-i-1
            total += remain*self.factorial(remain)
        return total
    
    def getPermutation(self, n: int, k: int) -> str:
        
        self.answer = None
        def backTrack(i,count,arr):
            
            if count > k or self.answer or count + self.findMax(i,n) < k  :
                return
            
            if i == n:
                
                if count == k:
                    self.answer = "".join(arr)
                return
            
            less = 0
            for num in range(1,n+1):
                if str(num) not in arr:
                    backTrack(i+1,count + less*self.factorial(n-i-1),arr+[str(num)])
                    less += 1
        
        backTrack(0,1,[])
        return self.answer