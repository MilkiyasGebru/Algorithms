class Solution:
    
    @lru_cache(None)
    def factorial(self,n):
        
        if n <= 1:
            return 1
        
        return n*self.factorial(n-1)
    
    def getPermutation(self, n: int, k: int) -> str:
        
        arr = [i for i in range(1,n+1)]
        num = ""
        k-=1
        
        for i in range(n-1,-1,-1):
            
            div = k // self.factorial(i)
            k -= div * self.factorial(i)
            num += str(arr[div])
            arr.remove(arr[div])
        
        return num
            
            