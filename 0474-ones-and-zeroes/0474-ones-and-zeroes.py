class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        
        @lru_cache(None)
        def dp(index,zero,one):
            
            if  zero < 0 or one < 0:
                return -inf
            
            if index >= len(strs)  :
                return 0
            
            a  = strs[index].count("0")
            b = strs[index].count("1")
            return max(1+ dp(index+1,zero-a,one-b),dp(index+1,zero,one))
        return  dp(0,m,n)
            
            
            
            