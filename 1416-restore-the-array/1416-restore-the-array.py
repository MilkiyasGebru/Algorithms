class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        mod = 10**9 + 7
        @lru_cache(None)
        def dp(index):
            
            if index == len(s):
                return 1
            
            if s[index] == "0":
                return 0
            count = 0
            for i in range(index+1,len(s)+1):
                num = s[index:i]
                if int(num)>k:
                    break
                count += dp(i)
            
            return count%mod
        
        return dp(0)