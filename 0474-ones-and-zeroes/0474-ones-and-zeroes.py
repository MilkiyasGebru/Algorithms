class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def calc(string):
            arr=[0,0]
            for i in string:
                arr[int(i)]+=1
            return arr[0],arr[1]
        arr = [calc(strs[i]) for i in range(len(strs))]
        @lru_cache(None)
        def dp(index,zero,one):
            
            if  zero < 0 or one < 0:
                return -inf
            
            if index >= len(strs)  :
                return 0
            
            a,b = arr[index]
            return max(1+ dp(index+1,zero-a,one-b),dp(index+1,zero,one))
        return  dp(0,m,n)
            
            
            
            