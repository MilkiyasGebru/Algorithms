class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        a = e = i = o = u = 1
        mod = 10**9 + 7
        for _ in range(n-1):
            
            a,e,i,o,u = e,a+i,a+e+o+u,i+u,a
            a %= mod
            e %= mod
            i %= mod
            o %= mod
            u %= mod
        return (a+e+i+o+u)%mod