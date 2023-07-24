class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        if n in [-1,0,1]:
            return x**n
        if n % 2 == 0:
            return self.myPow(x,n//2)**2
        return x*(self.myPow(x,n//2)**2)